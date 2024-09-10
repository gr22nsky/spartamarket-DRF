from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from .validators import validate_signup

class SignUpView(APIView):
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthenticated()]
        
    def post(self, request):
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({'message':err_msg}, status = 400)
        
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
    
    def delete(self, request, using=None, keep_parents=None):
        user = request.user
        if request.user.check_password(request.data.get('password')):
            user.soft_delete()
            return Response({'message':'회원탈퇴가 완료되었습니다.'})
        return Response({'message':'비밀번호가 일치하지않습니다.'}, status=400)
    
class LogInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'message':'username 또는 password가 올바르지 않습니다.'}, status=400)

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
        return Response({'message':'로그아웃되었습니다.'}, status=200)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):
        user = User.objects.get(username=username)
        if username == request.user.username:
            is_valid, err_msg = validate_signup(request.data)
            if not is_valid:
                return Response({'message':err_msg}, status = 400)
            
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response({'message':'수정권한이 없습니다.'}, status=401)