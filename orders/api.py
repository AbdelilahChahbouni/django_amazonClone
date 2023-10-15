from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Cart , CartDetail , Order , OrderDetail , Coupon
from product.models import Product 
from .serializers import CartSerializer , OrderListSerializer , OrderDetailSerializer
import datetime




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



class OrderListAPI(generics.ListAPIView):
 serializer_class = OrderListSerializer
 queryset = Order.objects.all()

 def list(self,request,*args,**kwargs):
  user = User.objects.get(username=self.kwargs["username"])
  queryset = self.get_queryset().filter(user=user)
  data = OrderListSerializer(queryset , many=True).data
  return Response(data)


 # def get_queryset(self):
 #  user = User.objects.get(username=self.kwargs["username"])
 #  queryset = super(OrderListAPI,self).get_queryset()
 #  queryset = queryset.filter(user=user)
 #  return queryset

class OrderDetailAPI(generics.RetrieveAPIView):
  #serializer_class = OrderListSerializer
  #queryset = Order.objects.all()
  serializer_class = OrderDetailSerializer
  queryset = Order.objects.all()


class CreateOrderAPI(generics.GenericAPIView):
 def get(self , request , *args , **kwargs):
  user = User.objects.get(username=self.kwargs["username"])
  cart = Cart.objects.get(user=user , status_cart = "InProgress")
  cart_detail = CartDetail.objects.filter(cart = cart)

  new_order = Order.objects.create(
   user = user,
   coupon = cart.coupon,
   total_after_coupon = cart.total_after_coupon

  )

  for item in cart_detail:
   OrderDetail.objects.create(
    order = new_order,
    product = item.product,
    price = item.product.price,
    quantity = item.quantity,
    total_price = round(int(item.quantity)*int(item.product.price),2)

   )

  cart.status_cart = "Completed"
  cart.save()
  return Response({"message": "the order is completed"})



class AplayCouponAPI(generics.GenericAPIView):
  def post(self , request , *args , **kwargs):
    user = User.objects.get(username=self.kwargs["username"])
    cart = Cart.objects.get(user=user , status_cart = "InProgress")
    coupon = get_object_or_404(Coupon , code=request.data["coupon_code"])

    if coupon and coupon.quantity > 0 :
     today_date = datetime.datetime.today().date()
     #today_date = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
     
     if today_date >= datetime.datetime.date((coupon.start_date)) and datetime.datetime.date((coupon.end_time)):
        coupon_value = cart.cart_total() * coupon.discount / 100
        cart_total = cart.cart_total() - coupon_value
        coupon.quantity -= 1
        coupon.save()
        cart.coupon = coupon
        cart.total_after_coupon = cart_total
        cart.save()
        return Response({"message":"the coupon aplied succssefully"})
     else:
      return Response({"message":"the date of coupon expired"})
    else:
     return Response({"message":"the Coupon is not valid"})



     


















