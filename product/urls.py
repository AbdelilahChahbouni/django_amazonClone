from django.urls import path
from .views import ProductList , ProductDetails


urlpatterns = [
	path('' ,ProductList.as_view() ),
	path('<int:pk>',ProductDetails.as_view()),

]