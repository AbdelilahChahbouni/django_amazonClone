from django.shortcuts import render
from django.db.models import Count 

from product.models import Product , Brand , Review
from django.views.decorators.cache import cache_page

# Create your views here.

@cache_page(60 * 2)
def home(request):
	brands = Brand.objects.all().annotate(product_count = Count("product_brand"))
	sale_product = Product.objects.filter(flag='Sales')[:10]
	new_product = Product.objects.filter(flag='New')[:6]
	feature_product = Product.objects.filter(flag='Feature')[:10]
	reviews = Review.objects.all()[:5]
	return render(request , "settings/home.html" , {
		"brands":brands,
		"sale_product":sale_product,
		"new_product":new_product,
		"feature_product":feature_product,
		"reviews":reviews
		})

	