from django.db import models

# Model for products add,update,delete and view
class Product(models.Model):
    LIVE =1
    DELETE =0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))# to set the choices for the status field, we can use this field to filter the products based on their status in the views and templates
    title=models.CharField(max_length=200)
    price=models.FloatField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    priority=models.IntegerField(default=0)# to set the default priority of the product to 0, we can use this field to sort the products based on their priority in the views and templates
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)# to set the default delete status of the product to LIVE, we can use this field to filter the products based on their delete status in the views and templates
    createtd_at=models.DateTimeField(auto_now_add=True)# to set the created_at field to the current date and time when the product is created, we can use this field to sort the products based on their creation date in the views and templates
    updated_at=models.DateTimeField(auto_now=True)# to set the updated_at field to the current date and time when the product is updated, we can use this field to sort the products based on their update date in the views and templates
    #auto_now_add is used to set the field to the current date and time when the object is created and auto_now is used to set the field to the current date and time when the object is updated
    
    def __str__(self) -> str:# to return the title of the product when we print the product object in the console or when we see the product object in the admin panel, it will show the title of the product instead of Product object
        return self.title # it will show the title of the product in admin panel instead of Product object














