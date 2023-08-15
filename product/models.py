from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

FLAG_TYPES = (('sale', 'sale'),
              ('New','New'),
              ('Feature','Feature'),
              )




class Product(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=10 , choices=FLAG_TYPES )
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    sku = models.CharField(max_length=12)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=3000)
    quantity = models.IntegerField()
    brand = models.ForeignKey('Brand' , related_name='product_brand' , on_delete=models.SET_NULL , null= True)


class ProductsImages(models.Model):
    pass


class Brand(models.Model):
    name =models.CharField(max_length=200)
    image = models.ImageField(upload_to='brands')



class Review(models.Model):
    user = models.ForeignKey(User , related_name="review_user" , on_delete=models.SET_NULL , null= True)
    product = models.ForeignKey(Product , related_name='product_review' , on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now())
