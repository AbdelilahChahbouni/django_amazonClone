from django.shortcuts import render
from django.db.models import Count 

from product.models import Product , Brand , Review

# Create your views here.


def home(request):
	brands = Brand.objects.all().annotate(product_count = Count("product_brand"))
	sale_product = Product.objects.filter(flag='Sales')[0:10]
	new_product = Product.objects.filter(flag='New')[0:10]
	feature_product = Product.objects.filter(flag='Feature')[:10]
	reviews = Review.objects.all()
	return render(request , "settings/home.html" , {
		"brands":brands,
		"sale_product":sale_product,
		"new_product":new_product,
		"feature_product":feature_product,
		"reviews":reviews
		})

	