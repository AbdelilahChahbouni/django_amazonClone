from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand , ProductsImages , Review
# Create your views here.


class ProductList(ListView):
	model = Product


class ProductDetails(DetailView):
	model = Product



