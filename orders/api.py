from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Cart , CartDetail
from product.models import Product
from .serializers import CartSerializer




class CartDetailCreateAPI(generics.GenericAPIView):
	serializer_class = CartSerializer


	def get(self, request , *args , **Kwargs):
		user = User.objects.get(username=self.kwargs["username"])
		cart , created = Cart.objects.get_or_create(user=user , status_cart = "InProgress")
		data = CartSerializer(cart).data
		return Response({"cart":data})


	def post(self , requset , *args , **kwargs):
		pass 


	def delete(self , requset , *args , **kwargs):
		pass 


