from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Order , Cart , CartDetail , Order , OrderDetail
from product.models import Product


# Create your views here.


class OrderList(LoginRequiredMixin,ListView):
	model = Order
	paginate_by = 10

	def get_queryset(self):
		queryset = super().get_queryset().filter(user=self.request.user)
		return queryset


def add_to_cart(request):
	quantity = request.POST["qty"]
	product = Product.objects.get(id= request.POST['prod_id'])

	cart = Cart.objects.get(user = request.user )
	cart_deatil , created = CartDetail.objects.get_or_create(cart = cart , product= product)

	cart_deatil.quantity = int(quantity)
	cart_deatil.total_price = round(int(quantity) * product.price ,2)
	cart_deatil.save()

	return redirect(f"/products/{product.slug}")




@login_required
def checkout(request):
	cart = Cart.objects.get(user=request.user)
	cart_detail = CartDetail.objects.filter(cart=cart)

	return render(request , "orders/checkout.html" , {"cart_data": cart_detail})

	