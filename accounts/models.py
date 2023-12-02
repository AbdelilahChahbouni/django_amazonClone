from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code



class Profile(models.Model):
    user = models.OneToOneField(User , related_name="user_profile" , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile")
    code = models.CharField(max_length=10 , default=generate_code)



ADDRESS_TYPES = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussiness','Bussiness'),
    ('Academy','Academy'),
    ('Others','Others'),
)

class Address(models.Model):
    user = models.ForeignKey(User , related_name="user_address" , on_delete=models.CASCADE)
    type = models.CharField(max_length=100 , choices=ADDRESS_TYPES)
    address = models.TextField(max_length=300)
    notes = models.TextField(max_length=200 , blank=True , null=True)


PHONE_TYPES = (
    ('Primary','Primary'),
    ('Secondary','Secondary'),
)


class Phone(models.Model):
    user = models.ForeignKey(User , related_name="user_phone" ,on_delete=models.CASCADE)
    type = models.CharField(max_length=100 , choices=PHONE_TYPES)
    phone = models.CharField(max_length=30)



