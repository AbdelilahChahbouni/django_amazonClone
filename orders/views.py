from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Order , Cart , CartDetail , Order , OrderDetail , Coupon
from product.models import Product
import datetime
from django.shortcuts import get_object_or_404
from settings.models import deliveryFee
from django.http import JsonResponse
from django.template.loader import render_to_string


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


def remove_from_cart(request , id):
	cart_detail = CartDetail.objects.get(id = id)
	cart_detail.delete()
	return redirect("/products")

@login_required
def checkout(request):
	cart = Cart.objects.get(user=request.user)
	cart_detail = CartDetail.objects.filter(cart=cart)
	fee_value = deliveryFee.objects.last().fee


	if request.method=="POST":
		coupon = get_object_or_404(Coupon , code=request.POST["coupon_code"])
		total = None
		cart_sub_total=None
		if coupon and coupon.quantity > 0 :
			today_date = datetime.datetime.today().date()
			if today_date >= datetime.datetime.date((coupon.start_date)) and datetime.datetime.date((coupon.end_time)):
				coupon_value = cart.cart_total() * coupon.discount / 100
				cart_total = cart.cart_total() - coupon_value
				coupon.quantity -= 1
				coupon.save()
				cart.coupon = coupon
				cart.total_after_coupon = cart_total
				cart.save()
				total = fee_value + cart_total

				
				cart = Cart.objects.get(user=request.user , status_cart = "InProgress")
				html = render_to_string("include/checkout_table.html",{

					"cart_data": cart_detail,
					"cart_sub_total": cart_total,
					"cart_total": total,
					"coupon": coupon_value,
					"fee_value":fee_value,
							})
				return JsonResponse({"result":html})


			
	else:
		cart_sub_total= cart.cart_total()
		total = fee_value + cart.cart_total()
		coupon = 0


	return render(request , "orders/checkout.html" ,{

					"cart_data": cart_detail,
					"cart_sub_total": cart_sub_total,
					"cart_total": total,
					"coupon": coupon,
					"fee_value":fee_value,
							})

	