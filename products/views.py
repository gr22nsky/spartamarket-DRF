from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductListView(APIView):
    
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        image = request.data.get('image')
        product = Product.objects.create(title=title, content=content, image=image)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    def get_object(self, request, pk):
        return get_object_or_404(Product, pk=pk)
    
    def get(self, request, pk):
        product = self.get_object(request, pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(request, pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object(request, pk)
        product.delete()
        message = {'글이 삭제되었습니다.'}
        return Response(message)
        