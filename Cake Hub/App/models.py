from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='products/')
	is_sale = models.BooleanField(default=False)
	sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

	def __str__(self):
		return self.name

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	date_added = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return f'{self.quantity} x {self.product.name}'