from django.urls import path , include
from .views import ProductList , ProductDetails , BrandList , BrandDetail


urlpatterns = [
	path('' ,ProductList.as_view() ),
	path('<slug:slug>',ProductDetails.as_view()),
	path('brands/', BrandList.as_view()),
	path('brands/<slug:slug>', BrandDetail.as_view()),
	path("__debug__/", include("debug_toolbar.urls")),

]