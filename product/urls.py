from django.urls import path , include
from .views import ProductList , ProductDetails , BrandList , BrandDetail , query_set
from .api import product_list_api , product_detail_api , ProductListAPI , ProductDetailAPI 


urlpatterns = [
	path('' ,ProductList.as_view() ),
	path('debug' , query_set),
	path('<slug:slug>',ProductDetails.as_view()),
	path('brands/', BrandList.as_view()),
	path('brands/<slug:slug>', BrandDetail.as_view()),
	path("__debug__/", include("debug_toolbar.urls")),


	# api urls

	path("api/list" , ProductListAPI.as_view()),
	path("api/list/<int:pk>" , ProductDetailAPI.as_view()),


]