from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from .validators import validate_signup

class SignUpView(APIView):
    def post(self, request):
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({err_msg}, status = 400)
        
        user = User.objects.create_user(
            username = request.data.get('username'),
            password = request.data.get('password'),
            nickname = request.data.get('nickname'),
            birth = request.data.get('birth'),
            first_name = request.data.get('first_name'),
            last_name = request.data.get('last_name'),
            email = request.data.get('email'),
            gender = request.data.get('gender'),
            introduction = request.data.get('introduction'),
            # **request.data
        )
        res_data = UserSerializer(user).data
        refresh = RefreshToken.for_user(user)
        res_data['access_token'] = str(refresh.access_token)
        res_data['refresh_token'] = str(refresh)
        return Response(res_data)
    
class LogInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'username 또는 password가 올바르지 않습니다.'})

        serializer = UserSerializer(user)
        res_data = {'username' : serializer.data.get('username')}
        refresh = RefreshToken.for_user(user)
        res_data['access_token'] = str(refresh.access_token)
        res_data['refresh_token'] = str(refresh)
        return Response(res_data)

class LogOutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token_str = request.data.get('refresh_token')
        try:
            refresh_token = RefreshToken(refresh_token_str)
        except TokenError as e:
            return Response({str(e)}, status=400)

        refresh_token.blacklist()
        return Response({'로그아웃되었습니다.'}, status=200)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)