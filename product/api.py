from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def product_list_api(request):
	products = Product.objects.all()[0:20] # list data
	data = ProductSerializer(products,many=True).data # jason data
	return Response({"products": data})


