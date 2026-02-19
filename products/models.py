from django.db import models

# Model for products
class Product(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='products/')