from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductListView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def post(self, request):
        title = request.data.get('title')
        author = request.user
        content = request.data.get('content')
        image = request.data.get('image')
        product = Product.objects.create(title=title, author=author, content=content, image=image)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        return get_object_or_404(Product, pk=pk)
    
    def get(self, request, pk):
        product = self.get_object(request, pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(request, pk)
        if product.author == request.user:
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response({'수정권한이 없습니다.'})
    
    def delete(self, request, pk):
        product = self.get_object(request, pk)
        if product.author == request.user:
            product.delete()
            message = {'글이 삭제되었습니다.'}
            return Response(message)
        return Response({'삭제권한이 없습니다.'})
        