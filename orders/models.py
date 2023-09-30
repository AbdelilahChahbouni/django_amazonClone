from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from product.models import Product 
from utils import generate_code

# Create your models here.

CART_STAUS = (('InProgress' , 'InProgress' ),( 'Completed' , 'Completed' ))

class Cart(models.Model):
	user = models.ForeignKey(User,related_name="user_cart",on_delete=models.SET_NULL,null=True,blank=True)
	status_cart = models.CharField(max_length=10,choices=CART_STAUS)

	def __str__(self):
		return str(self.user)

	def cart_total(self):
		total = 0
		for item in self.cart_detail.all():
			total += item.total_price
		return round(total,2)


class CartDetail(models.Model):
	cart = models.ForeignKey(Cart , related_name='cart_detail' , on_delete=models.CASCADE)
	product = models.ForeignKey(Product , related_name="cart_product" , on_delete=models.SET_NULL,null=True,blank=True)
	quantity = models.IntegerField()
	total_price = models.FloatField(null=True,blank=True)

	def __str__(self):
		return str(self.cart)






ORDER_STAUS = (("Recieved" , "Recieved"),("Processed" , "Processed"),("Shipped" , "Shipped"),("Delivered" , "Delivered"))

class Order(models.Model):
	user = models.ForeignKey(User,related_name="user_order",on_delete=models.SET_NULL,null=True,blank=True)
	status_order = models.CharField(max_length=10,choices=ORDER_STAUS)	
	code = models.CharField(default=generate_code.generate_code,max_length=40)
	order_time = models.DateTimeField(default=timezone.now)
	delivery_time = models.DateTimeField(null=True, blank=True) 
	coupon = models.ForeignKey('Coupon' , related_name='order_coupon' , on_delete=models.SET_NULL , null=True,blank=True)
	total_after_coupon = models.FloatField(null=True,blank=True)

	def __str__(self):
		return str(self.user)


class OrderDetail(models.Model):
	cart = models.ForeignKey(Order , related_name='order_detail' , on_delete=models.CASCADE)
	product = models.ForeignKey(Product , related_name="order_product" , on_delete=models.SET_NULL,null=True,blank=True)
	price = models.FloatField()
	quantity = models.IntegerField()
	total_price = models.FloatField(null=True,blank=True)

	def __str__(self):
		return str(self.cart)


class Coupon(models.Model):
	code = models.CharField(max_length=20)
	discount = models.IntegerField()
	quantity = models.IntegerField()
	start_date = models.DateTimeField(default=timezone.now)
	end_time = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.code 

	def save(self, *args , **kwargs):
		week = datetime.timedelta(days=7)
		self.end_time = self.start_date + week
		super(coupon, self).save(*args , **kwargs)