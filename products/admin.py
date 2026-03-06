from django.contrib import admin
from . models import Product
# Register your models here.
admin.site.register(Product)# to register the Product model in the admin site, so that we can add,update,delete and view the products from the admin panel of the application