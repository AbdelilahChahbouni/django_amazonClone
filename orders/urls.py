from django.urls import path
from .views import OrderList , checkout , add_to_cart , remove_from_cart , process_payment , payment_success , payment_failed
from .api import CartDetailCreateAPI , OrderListAPI , OrderDetailAPI , CreateOrderAPI , AplayCouponAPI
app_name='orders'

urlpatterns = [
	path('', OrderList.as_view()),
	path('checkout/' , checkout),
	path('checkout/payment' , process_payment ,name='process_payment'),
	path('checkout/payment/success' , payment_success),
	path('checkout/payment/failed' , payment_failed),

	path('add_to_cart' , add_to_cart, name='add_to_cart'),
	path('<int:id>/remove_from_cart' , remove_from_cart),

	# api 

	path('api/<str:username>/cart/' , CartDetailCreateAPI.as_view()),
    path('api/<str:username>/cart/aplay-coupon/' , AplayCouponAPI.as_view()),
    path('api/<str:username>/create-order/' , CreateOrderAPI.as_view()),
	path('api/list/<str:username>' , OrderListAPI.as_view()),
    path('api/list/<str:username>/<int:pk>', OrderDetailAPI.as_view()),
    




]