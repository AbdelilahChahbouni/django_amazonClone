from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

FLAG_TYPES = (('sale', 'sale'),
              ('New','New'),
              ('Feature','Feature'),
              )




class Product(models.Model):
    name = models.CharField(_('name'),max_length=120)
    flag = models.CharField(_('flag'),max_length=10 , choices=FLAG_TYPES )
    image = models.ImageField(_('image'),upload_to='products')
    price = models.FloatField(_('price'))
    sku = models.CharField(_('sku'),max_length=12)
    subtitle = models.CharField(_('subtitle'),max_length=300)
    description = models.TextField(_('description'),max_length=3000)
    quantity = models.IntegerField(_('quantity'))
    brand = models.ForeignKey('Brand' ,verbose_name=_('brand') ,related_name='product_brand' , on_delete=models.SET_NULL , null= True)


class ProductsImages(models.Model):
    product = models.ForeignKey(Product , verbose_name=_('product'),related_name="product_image" , on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to="product_image")

class Brand(models.Model):
    name =models.CharField(_('name'),max_length=200)
    image = models.ImageField(_('image'),upload_to='brands')



class Review(models.Model):
    user = models.ForeignKey(User , verbose_name=_('user'),related_name="review_user" , on_delete=models.SET_NULL , null= True)
    product = models.ForeignKey(Product , verbose_name=_('product'),related_name='product_review' , on_delete=models.CASCADE)
    rate = models.IntegerField(_('rate'))
    review = models.CharField(_('review'),max_length=200)
    created_at = models.DateTimeField(_('created at'),default=timezone.now())
    
