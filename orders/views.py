from django.shortcuts import redirect, render
from  products.models import Product
from  django.contrib import messages
from customers.models import Customers
from . models import Order,OrderedItem
from django.contrib.auth.decorators import login_required

# Create your views here.


def show_cart(request):# view function for handling the cart page of the application, when the user accesses the /cart URL of the application then this view function will be called and it will render the cart.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    user=request.user# to get the currently logged in user, we can use this user variable to get the cart of the user and display the products in the cart of the user in the cart page of the application
    customer,created=Customers.objects.get_or_create(user=user)# to get the customer profile of the user, we can use this customer variable to get the cart of the user and display the products in the cart of the user in the cart page of the application
    cart_obj,created= Order.objects.get_or_create(# to get the cart of the user from the database, if the cart does not exist then it will create a new cart for the user and return the cart object and a boolean value indicating whether the cart was created or not, we can use this cart_obj variable to get the products in the cart of the user and display them in the cart page of the application
        owner=customer,# to set the owner of the cart to the customer profile of the user, we can use this owner field to get the cart of the user from the database and display the products in the cart of the user in the cart page of the application
        order_status=Order.CART_STAGE# to set the order status of the cart to CART_STAGE, we can use this order_status field to get the cart ofthe user fromthe database and displaythe products inthecart ofthe user inthecart page ofthe application, CART_STAGE is a constant defined inthe Order model which indicates thatthe order is inthe cart stage, we can use this constant to filterthe orders inthe database and getthe cart ofthe user when they click onthe add tocart button inthe product detail page ofthe application
    )
    context={'cart':cart_obj}#creating a context dictionary to pass_the_cart_obj variable to template with_the key 'cart', so that we can access_the cart_obj variable in template using_the key 'cart' and display_the products in_the cart of_the user in_the cart page of_the application
    return render(request,'cart.html',context)#rendering the cart.html template for the cart page of the application, cart.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'

@login_required(login_url='account')# to restrict the access to the add_to_cart view function to only logged in users, if a user who is not logged in tries to access this view function then they will be redirected to the account page of the application where they can log in or sign up, we can use this login_required decorator to restrict the access to the add_to_cart view function to only logged in users when they click on the add to cart button in the product detail page of the application 
def add_to_cart(request):# view function for handling the add to cart functionality of the application, when the user clicks on the add to cart button in the product detail page of the application then this view function will be called and it will add the product with the given primary key (pk) to the cart of the user and redirect them to the cart page of the application, we can use this add_to_cart view function to add the products to the cart of the user when they click on the add to cart button in the product detail page of the application
    if request.POST:
        user=request.user# to get the currently logged in user, we can use this user variable to get the cart of the user and add the product to the cart of the user when they click on the add to cart button in the product detail page of the application
        customer,created=Customers.objects.get_or_create(user=user)# to get the customer profile of the user, we can use this customer variable to get the cart of the user and add the product to the cart of the user when they click on the add to cart button in the product detail page of the application

        product_id=request.POST.get('product_id')# to get the product id from the hidden input field in the product detail page of the application, we can use this product_id variable to get the product object from the database and add it to the cart of the user when they click on the add to cart button in the product detail page of the application
        quantity=int(request.POST.get('quantity'))# to get the quantity of the product from the input
        cart_obj,created= Order.objects.get_or_create(# to get the cart of the user from the database, if the cart does not exist then it will create a new cart for the user and return the cart object and a boolean value indicating whether the cart was created or not, we can use this cart_obj variable to add the product to the cart of the user when they click on the add to cart button in the product detail page of the application
            owner=customer,# to set the owner of the cart to the customer profile of the user, we can use this owner field to get the cart of the user from the database and add the product to the cart of the user when they click on the add to cart button in the product detail page of the application
            order_status=Order.CART_STAGE# to set the order status of the cart to CART_STAGE, we can use this order_status field to get the cart of the user from the database and add the product to the cart of the user when they click on the add to cart button in the product detail page of the application, CART_STAGE is a constant defined in the Order model which indicates that the order is in the cart stage, we can use this constant to filter the orders in the database and get the cart of the user when they click on the add to cart button in the product detail page of the application
        )
        product=Product.objects.get(pk=product_id)# to get the product object from the database using the product id that we got from the hidden input field in the product detail page of the application, we can use this product variable to add the product to the cart of the user when they click on the add to cart button in the product detail page of the application
        ordered_item,created=OrderedItem.objects.get_or_create(# to create a new ordered item for the product that is being added to the cart of the user, we can use this ordered_item variable to add the product to the cart of the user when they click on the add to cart button in the product detail page of the application
            product=product,# to set the product id of the ordered item to the product id that is being added to the cart of the user, we can use this product_id variable to get the product object from the database and add it to the cart of the user when they click on the add to cart button in the product detail page of the application                     
            owner=cart_obj,# to set the owner of the ordered item to the cart object that we got or created for the user, we can use this cart_obj variable to add the product to the cart of the user when they click on the add to cart button in the product detail page of the application
        )
        if created:# to check if the ordered item was created or not, if it was created then we need to set the quantity of the ordered item to the quantity that we got from the input field in the product detail page of the application, if it was not created then we need to update the quantity of the ordered item by adding the quantity that we got from the input field in the product detail page of the application, we can use this if condition to set or update the quantity of the ordered item when they click on the add to cart button in the product detail page of the application
            ordered_item.quantity=quantity# to set the quantity of the ordered item to the quantity that we got from the input field in the product detail page of the application, we can use this quantity variable to set or update the quantity of the ordered item when they click on the add to cart button in the product detail page of the application    
            ordered_item.save()# to save the ordered item object to the database, we can use this save() method to save the ordered item object to the database after setting or updating the quantity of the ordered item when they click on the add to cart button in the product detail page of the application
        else:
            ordered_item.quantity += quantity# to update the quantity of the ordered item by adding the quantity that we got from the input field in the product detail page of the application, we can use this quantity variable to set or update the quantity of the ordered item when they click on the add to cart button in the product detail page of the application
            ordered_item.save()# to save the ordered item object to the database, we can use this save() method to save the ordered item object to the database after setting or updating the quantity of the ordered item when they click on the add to cart button in the product detail page of the application
        # Add the product to the cart
    return redirect('cart')# to redirect the user to the cart page of the application after adding the product to the cart of the user, we can use this redirect function to redirect the user to the cart page of the application after adding the product to the cart of the user when they click on the add to cart button in the product detail page of the application



def remove_from_cart(request, item_id):# view function for handling the remove from cart functionality of the application, when the user clicks on the remove button in the cart page of the application then this view function will be called and it will remove the product with the given primary key (pk) from the cart of the user and redirect them to the cart page of the application, we can use this remove_from_cart view function to remove the products from the cart of the user when they click on the remove button in the cart page of the application
    item = OrderedItem.objects.get(pk=item_id)# to get the ordered item object from the database using the item id that we got from the hidden input field in the cart page of the application, we can use this item variable to remove the product from the cart of the user when they click on the remove button in the cart page of the application
    if item:
        item.delete()# to delete the ordered item object from the database, we can use this delete() method to remove the product from the cart of the user when they click on the remove button in the cart page of the application
    return redirect('cart')# to redirect the user to the cart page of the application af


def checkout_cart(request):# view function for handling the checkout functionality of the application, when the user clicks on the checkout button in the cart page of the application then this view function will be called and it will change the order status of the cart of the user to ORDER_CONFIRMED and redirect them to the account page of the application, we can use this checkout_cart view function to change the order status of the cart of the user to ORDER_CONFIRMED and redirect them to the account page of the application when they click on the checkout button in the cart page of the application
    if request.POST:# to check if the request method is POST, if it is then we need to get the cart of the user from the database and change the order status of the cart of the user to ORDER_CONFIRMED, we can use this if condition to change the order status of the cart of the user to ORDER_CONFIRMED when they click on the checkout button in the cart page of the application  
        try:
                user=request.user# to get the currently logged in user, we can use this user variable to get the cart of the user and change the order status of the cart of the user to ORDER_CONFIRMED when they click on the checkout button in the cart page of the application
                customer=user.customer_profile
                total=float(request.POST.get('total'))# to get the total price of the cart from the hidden input field in the cart page of the application, we can use this total variable to display the total price of the cart in the order confirmation page of the application after they click on the checkout button in the cart page of the application
                order_obj= Order.objects.get(
                    owner=customer,
                    order_status=Order.CART_STAGE
                )
                item_exists=OrderedItem.objects.filter(owner=order_obj).exists()# to check if there are any ordered items in the cart of the user, we can use this item_exists variable to check if there are any ordered items in the cart of the user before changing the order status of the cart of the user to ORDER_CONFIRMED when they click on the checkout button in the cart page of the application
                if order_obj and item_exists and total>0:# to check if the cart of the user exists and there are any ordered items in the cart of the user and the total price of the cart is greater than 0, if all these conditions are true then we can change the order status of the cart of the user to ORDER_CONFIRMED, we can use this if condition to change the order status of the cart of the user to ORDER_CONFIRMED when they click on the checkout button in the cart page of the application
                    order_obj.order_status=Order.ORDER_CONFIRMED
                    order_obj.total_price=total
                    order_obj.save()
                    status_message="Order confirmed successfully!.Order will be processed soon. "
                    messages.success(request, status_message)
                else:
                    status_message="Order not found. No items in cart.Please add items to cart before checkout."
                    messages.error(request, status_message)
        except Exception as e:
            status_message="An error occurred while confirming the order. Please try again."
            messages.error(request, status_message)
    return redirect('cart')

@login_required(login_url='account')# to restrict the access to the orders view function to only logged in users, if a user who is not logged in tries to access this view function then they will be redirected to the account page of the application where they can log in or sign up, we can use this login_required decorator to restrict the access to the orders view function to only logged in users when they click on the orders link in the account page of the application
def view_orders(request):# view function for handling the orders page of the application, when the user clicks on the orders link in the account page of the application then this view function will be called and it will render the orders.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    user=request.user# to get the currently logged in user, we can use this user variable to get the orders of the user and display them in the orders page of the application
    customer=user.customer_profile
   
@login_required(login_url='account')# to restrict the access to the orders view function to only logged in users, if a user who is not logged in tries to access this view function then they will be redirected to the account page of the application where they can log in or sign up, we can use this login_required decorator to restrict the access to the orders view function to only logged in users when they click on the orders link in the account page of the application
def show_orders(request):# view function for handling the cart page of the application, when the user accesses the /cart URL of the application then this view function will be called and it will render the cart.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    user=request.user# to get the currently logged in user, we can use this user variable to get the cart of the user and display the products in the cart of the user in the cart page of the application
    customer=user.customer_profile# to get the customer profile of the user, we can use this customer variable to get the cart of the user and display the products in the cart of the user in the cart page of the application
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}#creating a context dictionary to pass the all_orders variable to template with the key 'orders', so that we can access the all_orders variable in template using the key 'orders' and display the orders of the user in the orders page of the application
    
    return render(request,'orders.html',context)#rendering the orders.html template for the orders page of the application, orders.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'










