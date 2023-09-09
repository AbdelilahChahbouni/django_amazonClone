
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

	print(f'seed {number} brands successfully ')



def seed_product(number):
	fake = Faker()
	images = os.listdir(os.chdir("media/products"))
	flags = ['New' , 'Features', 'Sales']

	for _ in range(number):
		Product.objects.create(
			name = fake.name(),
			image =f'products/{images[random.randint(0,13)]}',
			flag = flags[random.randint(0,2)],
			price = round(random.uniform(20.99 , 99.99),2),
			sku = random.randint(1000,10000),
			subtitle = fake.text(max_nb_chars=500),
			description = fake.text(max_nb_chars=1000),
			quantity = random.randint(0 , 50),
			brand = Brand.objects.get(id = random.randint(2 , 1000))
			)


	print(f'seed {number} Products successfully')


#seed_brand(500)

seed_product(1500)





