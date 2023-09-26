from django.urls import path , include
from .views import ProductList , ProductDetails , BrandList , BrandDetail , query_set
from .api import ProductListAPI , ProductDetailAPI , BrandListAPI , BrandDetailAPI 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


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
	path("brands/api/list" , BrandListAPI.as_view()),
	path("brands/api/list/<int:pk>" , BrandDetailAPI.as_view()),

	# api token

	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

	


]