from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):
    
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        image = request.data.get('image')
        product = Product.objects.create(title=title, content=content, image=image)
        res_json = {
            'title' : product.title,
            'content' : product.content,
            'imgae' : product.image.name
        }
        return Response(res_json, status = 201)