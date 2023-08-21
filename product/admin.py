from django.contrib import admin
from .models import Product , Brand , ProductsImages , Review



class ProductImagesTabular(admin.TabularInline):
	model = ProductsImages


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name' , 'flag' , 'price' , 'quantity']
	list_filter = ['flag' , 'brand']
	search_fields = ['name' , 'subtitle' , 'description']
	inlines = [ProductImagesTabular]







# Register your models here.
admin.site.register(Product , ProductAdmin)
admin.site.register(Brand)
admin.site.register(ProductsImages)
admin.site.register(Review)

