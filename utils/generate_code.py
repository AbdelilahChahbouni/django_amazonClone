import random


def generate_code(lenght):
	charcters = "123456789QWERTYUIOP"
	data = "".join(random.choice(charcters) for _ in range(lenght))
	return str(data) 



