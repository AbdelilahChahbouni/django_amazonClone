from django.db import models

# Create your models here.

class CompanyInfo(models.Model):
	name= models.CharField(max_length=200)
	logo = models.ImageField(upload_to="company_logo")
	subtitle = models.TextField(max_length=600)
	facebook_link = models.URLField(max_length=100, null=True , blank=True)
	twitter_link = models.URLField(max_length=100, null=True , blank=True)
	youtube_link = models.URLField(max_length=100, null=True , blank=True)
	phones = models.TextField(max_length=500 , null=True , blank=True)
	email = models.TextField(max_length=500 , null=True , blank=True)
	adress = models.TextField(max_length=500 , null=True , blank=True)
	call_us = models.TextField(max_length=100 , null=True , blank=True)
	eamil_us = models.TextField(max_length=100 , null=True , blank=True)
	android_app = models.URLField(max_length=100 , null=True , blank=True)
	iso_app = models.URLField(max_length=100 , null=True , blank=True)


	def __str__(self):
		return self.name
	
class deliveryFee(models.Model):
	fee = models.FloatField()


	def __str__(self):
		return str(self.fee)