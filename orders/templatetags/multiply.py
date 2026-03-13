from django import template

register = template.Library()# to register the custom template tag in the application, so that we can use this custom template tag in our templates

@register.simple_tag(name='multiply')# to register the custom template filter in the application, so that we can use this custom template filter in our templates with the name 'raw_chunks'
def multiply(a,b):# custom template filter function to multiply two numbers, so that we can calculate the subtotal of the ordered item in the cart page of the application by multiplying the price of the product with the quantity of the ordered item
    return a*b# to return the result of multiplying the two numbers, we can use this return statement to return the result of multiplying the price of the product with the quantity of the ordered item in the cart page of the application


