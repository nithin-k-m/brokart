from django.db import models
from customers.models import Customers
from products.models import Product



# Model for orders in cart(add,remove,update),change order status,cancel .etc
class Order(models.Model):
    LIVE =1
    DELETE =0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))# to set the choices for the delete_status field, we can use this field to filter the carts based on their delete status in the views and templates
    CART_STAGE=0# to set the value of CART_STAGE constant to 0, we can use this constant to set the order status of the order to CART_STAGE in the views and templates
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,'ORDER_PROCESSED'),(ORDER_DELIVERED,'ORDER_DELIVERED'),(ORDER_REJECTED,'ORDER_REJECTED'))# to set the choices for the order_status field, we can use this field to filter the orders based on their order status in the views and templates
    
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)# to set the default order status of the order to CART_STAGE, we can use this field to filter the orders based on their order status in the views and templates
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,related_name='orders')# to create a foreign key relationship between the Cart model and the Customers model, on_delete=models.SET_NULL means that if the customer is deleted then the corresponding cart will not be deleted but the owner field will be set to null, related_name='orders' allows us to access the orders of a customer from the customer object using customer.orders
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)# to set the default delete status of the product to LIVE, we can use this field to filter the products based on their delete status in the views and templates
    createtd_at=models.DateTimeField(auto_now_add=True)# to set the created_at field to the current date and time when the product is created, we can use this field to sort the products based on their creation date in the views and templates
    updated_at=models.DateTimeField(auto_now=True)# to set the updated_at field to the current date and time when the product is updated, we can use this field to sort the products based on their update date in the views and templates

class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name='addead_carts',on_delete=models.SET_NULL,null=True)# to create a foreign key relationship between the CartProduct model and the Product model, on_delete=models.SET_NULL means that if the product is deleted then the corresponding cart product will not be deleted but the product field will be set to null, related_name='added_carts' allows us to access the carts in which a product is added from the product object using product.added_carts
    quantity=models.IntegerField(default=1)# to set the default quantity of the product in the cart to 1, we can use this field to calculate the total price of the cart in the views and templates
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')# to create a foreign key relationship between the CartProduct model and the Cart model, on_delete=models.CASCADE means that if the cart is deleted then the corresponding cart product will also be deleted, related_name='cart_products' allows us to access the products in a cart from the cart object using cart.cart_products


















