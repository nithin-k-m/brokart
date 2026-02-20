from django.db import models
from django.contrib.auth.models import User

# Model for customers add,update,login,logout and signup
class Customers(models.Model):
    LIVE=1 # to set the value of LIVE constant to 1, we can use this constant to set the delete status of the customer to LIVE in the views and templates
    DELETE=0 # to set the value of DELETE constant to 0, we can use this constant to set the delete status of the customer to DELETE in the views and templates
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))# to set the choices for the delete_status field, we can use this field to filter the customers based on their delete status in the views and templates
    name=models.CharField(max_length=200)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')# to create a one-to-one relationship between the Customers model and the User model, we can use the OneToOneField to link the customer profile to the user account, on_delete=models.CASCADE means that if the user account is deleted then the corresponding customer profile will also be deleted, related_name='customer_profile' allows us to access the customer profile from the user object using user.customer_profile
    phone=models.CharField(max_length=15)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)# to set the default delete status of the customer to LIVE, we can use this field to filter the customers based on their delete status in the views and templates
    created_at=models.DateTimeField(auto_now_add=True)# to set the created_at field to the current date and time when the customer is created, we can use this field to sort the customers based on their creation date in the views and templates
    updated_at=models.DateTimeField(auto_now=True)# to set the updated_at field to the current date and time when the customer is updated, we can use this field to sort the customers based on their update date in the views and templates
    #auto_now_add is used to set the field to the current date and time when the object is created and auto_now is used to set the field to the current date and time when the object is updated

    def __str__(self) -> str:# to return the name of the customer when we print the customer object in the console or when we see the customer object in the admin panel, it will show the name of the customer instead of Customers object
        return self.name # it will show the name of the customer in admin panel instead of Customers object

