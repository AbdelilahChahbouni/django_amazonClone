from django.urls import path , include
from .views import ProductList , ProductDetails , BrandList , BrandDetail , query_set , add_review
from .api import ProductListAPI , ProductDetailAPI , BrandListAPI , BrandDetailAPI 

app_name="product"

urlpatterns = [
	path('' ,ProductList.as_view() ),
	path('debug' , query_set),
	path('<slug:slug>',ProductDetails.as_view()),
    path("<slug:slug>/add_review" , add_review , name="add_review"),
	path('brands/', BrandList.as_view()),
	path('brands/<slug:slug>', BrandDetail.as_view()),
	path("__debug__/", include("debug_toolbar.urls")),
  
    
   


	# api urls

	path("api/list" , ProductListAPI.as_view()),
	path("api/list/<int:pk>" , ProductDetailAPI.as_view()),
	path("brands/api/list" , BrandListAPI.as_view()),
	path("brands/api/list/<int:pk>" , BrandDetailAPI.as_view()),

	

	


]