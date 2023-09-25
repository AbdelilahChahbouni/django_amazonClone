from .models import Product , Brand
from .serializers import ProductListSerializer, ProductDetailSerializer , BrandListSerializer , BrandDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from rest_framework import generics
from .my_custom_filters import ProductFilters
from .custom_pagination import CustomPagination

#@api_view(['GET'])
#def product_list_api(request):
	#products = Product.objects.all()[0:20] # list data
	#data = ProductSerializer(products,many=True , context={"request":request}).data # jason data
	#return Response({"products": data})


#@api_view(["GET"])
#def product_detail_api(request , pro_id):
	#product = Product.objects.get(id=pro_id)
	#data = ProductSerializer(product , context={"request":request}).data
	#return Response({"product":data})


# class method api

class ProductListAPI(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductListSerializer
	filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
	filterset_fields = ['flag', 'brand']
	search_fields = ['name', 'subtitle','description']
	ordering_fields = ['price', 'quantity']
	filterset_class = ProductFilters
	pagination_class = CustomPagination


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer

class BrandListAPI(generics.ListAPIView):
	queryset = Brand.objects.all()
	serializer_class = BrandListSerializer

class BrandDetailAPI(generics.RetrieveAPIView):
	queryset = Brand.objects.all()
	serializer_class = BrandDetailSerializer



