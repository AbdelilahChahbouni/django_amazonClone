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


	def post(self , request , *args , **kwargs):
		user = User.objects.get(username=self.kwargs["username"])
		product = Product.objects.get(id = request.data["product_id"])
		new_qty = int(request.data['quantity'])
		cart = Cart.objects.get(user=user , status_cart="InProgress")
		cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)
		cart_detail.quantity = new_qty
		cart_detail.total_price = round((new_qty * product.price),2)
		cart_detail.save()

		cart = Cart.objects.get(user=user , status_cart="InProgress")
		data = CartSerializer(cart).data
		return Response({"message":"product added succssfully", "cart":data})







	def delete(self , request , *args , **kwargs):
		user = User.objects.get(username=self.kwargs["username"])
		cart_detail = CartDetail.objects.get(id=request.data["cart_detail_id"])
		cart_detail.quantity = 2
		cart_detail.delete()
		cart = Cart.objects.get(user=user , status_cart="InProgress")
		data = CartSerializer(cart).data
		return Response({"message":"cart detail deleted succssfully", "cart":data})





