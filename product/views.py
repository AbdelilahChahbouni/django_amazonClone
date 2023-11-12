from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand , ProductsImages , Review
from django.db.models import Q , F , Value
from django.db.models.aggregates import Min , Max , Sum , Count , Avg 
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(60 * 2)
def query_set(request):
	#data = Product.objects.select_related("brand").all()
	#data = Product.objects.filter(price__gt=30)
	#data = Product.objects.filter(price__lt=30)
	#data = Product.objects.filter(price__gte=30)
	#data = Product.objects.filter(price__lte=30)
	#data = Product.objects.filter(price = 30)
	#data = Product.objects.filter(price__range=(30 , 50))
	
	# navigate with relationship
	
	#data = Product.objects.filter(brand__name="Phones")
	
	#filter with text

	#data = Product.objects.filter(name__contains="Brown")
	#data = Product.objects.filter(name__startswith="P")
	#data = Product.objects.filter(name__endswith="e")
	#data = Product.objects.filter(tags__isnull=True)
	#data = Review.objects.filter(created_at__year=2023)
	#data = Review.objects.filter(created_at__month=8)


	#filter with 2 fields

	#data = Product.objects.filter(price__gt=20 , quantity__lt=10)
	#data = Product.objects.filter(Q(price__lt=30) or Q(quantity__lt=5))
	#data = Product.objects.filter(Q(price__lt=30) & Q(quantity__lt=5))
	#data = Product.objects.filter(~Q(price__lt=30) or Q(quantity__lt=5))

	#Field Lookup
	#data = Product.objects.filter(price = F('quantity'))

	#ordering

	#data = Product.objects.all().order_by("name")
	#data = Product.objects.order_by("name")
	# data = Product.objects.all().order_by("-name")
	# data = Product.objects.all().order_by("name").reverse()
	# data = Product.objects.all().order_by("name" , "-quantity")

	# ordering and slicing 

	# data = Product.objects.all().order_by("name")[0] # first item
	# data = Product.objects.all().order_by("name")[-1] # last item

	# data = Product.objects.all().earliest("name") # first element
	# data = Product.objects.all().latest("name") # last element

	# slicing

	# data = Product.objects.all()[0:10]

	# filter using columns

	# data = Product.objects.values("name" , "price") # dictionary 
	# data = Product.objects.values_list("name","price") # tuple
	# data = Product.objects.only("name","price")

	# remove duplicate

	# data = Product.objects.all().distinct()
	# data = Product.objects.defer("price") # return all fields without price field


	# aggregations

	# data = Product.objects.aggregate(Sum("quantity"))
	# data = Product.objects.aggregate(Avg("price"))


	# annotate

	#data = Product.objects.annotate(is_new=Value(True))
	#data = Product.objects.annotate(price_tax=F("price") * 1.5)
	data = Product.objects.all()
	context = {
		'data' : data
	}
	return render(request , "product/debug.html" , context)






class ProductList(ListView):
	model = Product
	paginate_by = 30


class ProductDetails(DetailView):
	model = Product
	def get_context_data(self , **kwargs):
		context= super().get_context_data(**kwargs)
		context['reviews']= Review.objects.filter(product=self.get_object())
		context['related_products']= Product.objects.filter(brand=self.get_object().brand)
		return context 


class BrandList(ListView):
	model = Brand
	queryset = Brand.objects.annotate(product_count=Count("product_brand"))



class BrandDetail(ListView):
	model = Product
	template_name = 'product/brand_detail.html'

	def get_queryset(self):
		brand = Brand.objects.get(slug=self.kwargs['slug'])
		return super().get_queryset().filter(brand=brand)

	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['brand'] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count("product_brand"))[0]
		return context 




