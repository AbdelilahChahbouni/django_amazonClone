
import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from product.models import Product , Brand , ProductsImages
from faker import Faker
import random 







def seed_brand(number):
	fake = Faker()
	images= os.listdir(os.chdir("media/products"))
	for _ in range(number):
		Brand.objects.create(
			name = fake.name(),
			image = f'brands/{images[random.randint(0,13)]}'
			)

	print(f'seed {number} products successfully ')



def seed_product():
	pass 





seed_brand(10)

