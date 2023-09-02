from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand , ProductsImages , Review
# Create your views here.

def query_set(request):
	#data = Product.objects.select_related("brand").all()
	#data = Product.objects.filter(price__gt=30)
	#data = Product.objects.filter(price__lt=30)
	#data = Product.objects.filter(price__gte=30)
	#data = Product.objects.filter(price__lte=30)
	#data = Product.objects.filter(price = 30)
	data = Product.objects.filter(price__range=(30 , 50))
	context = {
		'data' : data
	}
	return render(request , "product/debug.html" , context)






class ProductList(ListView):
	model = Product


class ProductDetails(DetailView):
	model = Product
	def get_context_data(self , **kwargs):
		context= super().get_context_data(**kwargs)
		context['reviews']= Review.objects.filter(product=self.get_object())
		context['related_products']= Product.objects.filter(brand=self.get_object().brand)
		return context 


class BrandList(ListView):
	model = Brand



class BrandDetail(ListView):
	model = Product
	template_name = 'product/brand_detail.html'

	def get_queryset(self):
		brand = Brand.objects.get(slug=self.kwargs['slug'])
		return super().get_queryset().filter(brand=brand)

	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['brand'] = Brand.objects.get(slug=self.kwargs['slug'])
		return context 




