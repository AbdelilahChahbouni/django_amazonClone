from django.urls import path
from .views import ProductList , ProductDetails , BrandList


urlpatterns = [
	path('' ,ProductList.as_view() ),
	path('<slug:slug>',ProductDetails.as_view()),
	path('brands/', BrandList.as_view()),

]