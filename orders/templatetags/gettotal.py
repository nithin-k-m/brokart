from django import template

register = template.Library()# to register the custom template tag in the application, so that we can use this custom template tag in our templates

@register.simple_tag(name='gettotal')# to register the custom template filter in the application, so that we can use this custom template filter in our templates with the name 'raw_chunks'
def gettotal(cart):# custom template filter function to multiply two numbers, so that we can calculate the subtotal of the ordered item in the cart page of the application by multiplying the price of the product with the quantity of the ordered item
    total=0# to initialize the total price of the cart to 0, we can use this total variable to calculate the total price of the cart by adding the subtotal of each ordered item in the cart page of the application
    for item in cart.added_items.all():# to iterate through all the ordered items in the cart of the user, we can use this for loop to calculate the total price of the cart by multiplying the price of each product with the quantity of each ordered item and adding them together in the cart page of the application
        total += item.product.price * item.quantity# to add the subtotal of each ordered item to the total price of the cart, we can use this line to calculate the total price of the cart by adding the subtotal of each ordered item in the cart page ofthe application
    return total# to return the total price ofthe cart, we can use this return statement to returnthe result of addingthe subtotal of each ordered item inthe cart page ofthe application