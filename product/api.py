from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

@api_view(['GET'])
def product_list_api(request):
	products = Product.objects.all()[0:20] # list data
	data = ProductSerializer(products,many=True , context={"request":request}).data # jason data
	return Response({"products": data})


@api_view(["GET"])
def product_detail_api(request , pro_id):
	product = Product.objects.get(id=pro_id)
	data = ProductSerializer(product , context={"request":request}).data
	return Response({"product":data})


# class method

class ProductListAPI(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer




