from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models import Avg 
from datetime import datetime
from django.utils.deconstruct import deconstructible
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
    tags = TaggableManager()
    slug = models.SlugField(null=True , blank=True)
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Product , self).save(*args , **kwargs)

    def avg_rate(self):
        avg = self.product_review.aggregate(rate_avg = Avg("rate"))
        if not avg["rate_avg"]:
            result = 0
            return result

        return avg["rate_avg"]

    def __str__(self):
        return self.name




class ProductsImages(models.Model):
    product = models.ForeignKey(Product , verbose_name=_('product'),related_name="product_image" , on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to="product_image")

    def __str__(self):
        return str(self.product)




class Brand(models.Model):
    name =models.CharField(_('name'),max_length=200)
    image = models.ImageField(_('image'),upload_to='brands')
    slug = models.SlugField(null=True , blank= True )


    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Brand , self).save(*args , **kwargs)


    def __str__(self):
        return self.name 





class Review(models.Model):
    user = models.ForeignKey(User , verbose_name=_('user'),related_name="review_user" , on_delete=models.SET_NULL , null= True)
    product = models.ForeignKey(Product , verbose_name=_('product'),related_name='product_review' , on_delete=models.CASCADE)
    rate = models.IntegerField(_('rate'))
    review = models.CharField(_('review'),max_length=200)
    created_at = models.DateTimeField(_('created at'),default=timezone.now)
    
    def __str__(self):
        return str(self.user)



