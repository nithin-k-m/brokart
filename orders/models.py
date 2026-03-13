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
    total_price=models.FloatField(default=0.0)# to set the default total price of the order to 0.0, we can use this field to calculate the total price of the order in the views and templates when they click on the checkout button in the cart page of the application
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,related_name='orders',null=True,blank=True)# to create a foreign key relationship between the Cart model and the Customers model, on_delete=models.SET_NULL means that if the customer is deleted then the corresponding cart will not be deleted but the owner field will be set to null, related_name='orders' allows us to access the orders of a customer from the customer object using customer.orders
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)# to set the default delete status of the product to LIVE, we can use this field to filter the products based on their delete status in the views and templates
    createtd_at=models.DateTimeField(auto_now_add=True)# to set the created_at field to the current date and time when the product is created, we can use this field to sort the products based on their creation date in the views and templates
    updated_at=models.DateTimeField(auto_now=True)# to set the updated_at field to the current date and time when the product is updated, we can use this field to sort the products based on their update date in the views and templates
    


    def get_total_price(self):# to calculate the total price of the ordered item, we can use this get_total_price method to calculate the total price of the ordered item in the views and templates when they click on the add to cart button in the product detail page of the application
        items=self.added_items.all()# to get all the ordered items in the cart, we can use this items variable to calculate the total price of the cart in the views and templates when they click on the checkout button in the cart page of the application
        total=0
        for item in items:# to iterate through all the ordered items in the cart, we can use this for loop to calculate the total price of the cart in the views and templates when they click on the checkout button in the cart page of the application
            total += item.product.price * item.quantity# to add the total price of each ordered item to the total price of the cart, we can use this line to calculate the total price of the cart by adding the total price of each ordered item in the cart page ofthe application
        return total# to return the total price of the cart, we can use this return statement to display the total price of the cart in the views and templates when they click onthe checkout button inthe cart page ofthe application

    
    
    def __str__(self) -> str:# to return the id of the order when we print the order object in the console or when we see the order object in the admin panel, it will show the id of the order instead of Order object
        return "order-{}-{}".format(self.id, self.owner.user.username) # it will show the id of the order in admin panel instead of Order object

class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name='addead_carts',on_delete=models.SET_NULL,null=True)# to create a foreign key relationship between the CartProduct model and the Product model, on_delete=models.SET_NULL means that if the product is deleted then the corresponding cart product will not be deleted but the product field will be set to null, related_name='added_carts' allows us to access the carts in which a product is added from the product object using product.added_carts
    quantity=models.IntegerField(default=1)# to set the default quantity of the product in the cart to 1, we can use this field to calculate the total price of the cart in the views and templates
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')# to create a foreign key relationship between the CartProduct model and the Cart model, on_delete=models.CASCADE means that if the cart is deleted then the corresponding cart product will also be deleted, related_name='cart_products' allows us to access the products in a cart from the cart object using cart.cart_products
   
    
















