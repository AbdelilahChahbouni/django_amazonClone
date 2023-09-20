from .models import Product , Brand , Review
from rest_framework import serializers
from django.db.models.aggregates import Avg



class ProductListSerializer(serializers.ModelSerializer):
	brand = serializers.StringRelatedField()
	rate_avg = serializers.SerializerMethodField()
	reviews_count = serializers.SerializerMethodField()
	#price_with_tax = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = "__all__"

	def get_rate_avg(self, product):
		avg =product.product_review.aggregate(rate_avg = Avg("rate"))
		if not avg["rate_avg"]:
			result = 0
			return result
		return avg["rate_avg"]

	def get_reviews_count(self , product:Product):
		review_count = product.product_review.all().count()
		return review_count

	#def get_price_with_tax(self , product):
		#return product.price * 1.5

class ReviewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = "__all__"

class ProductDetailSerializer(serializers.ModelSerializer):
	brand = serializers.StringRelatedField()
	rate_avg = serializers.SerializerMethodField()
	reviews_count = serializers.SerializerMethodField()
	reviews = ReviewsSerializer(source = "product_review" , many= True)
	class Meta:
		model = Product
		fields = "__all__"

	def get_rate_avg(self, product):
		avg =product.product_review.aggregate(rate_avg = Avg("rate"))
		if not avg["rate_avg"]:
			result = 0
			return result
		return avg["rate_avg"]

	def get_reviews_count(self , product:Product):
		review_count = product.product_review.all().count()
		return review_count




class BrandDetailSerializer(serializers.ModelSerializer):
	products = ProductListSerializer(source = "product_brand" , many= True)
	class Meta:
		model = Brand
		fields = "__all__"


class BrandListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = "__all__"




