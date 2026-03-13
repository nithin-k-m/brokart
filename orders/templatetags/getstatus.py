from django import template

register = template.Library()# to register the custom template tag in the application, so that we can use this custom template tag in our templates

@register.simple_tag(name='getstatus')# to register the custom template filter in the application, so that we can use this custom template filter in our templates with the name 'raw_chunks'
def getstatus(status):# custom template filter function to multiply two numbers, so that we can calculate the subtotal of the ordered item in the cart page of the application by multiplying the price of the product with the quantity of the ordered item
    status=status-1# to decrement the status variable by 1, we can use this line to get the index of the order status in the status_array list by decrementing the status variable by 1, because the order status in the Order model is defined as an integer field with choices and the choices are defined as a list of tuples where the first element of each tuple is an integer representing the order status and the second element is a string representing the order status, so we need to decrement the status variable by 1 to get the correct index of the order status in the status_array list
    status_array=['confirmed','processed','delivered']# to create an array of order status, we can use this array to get the order status of the order in the orders page of the application by using the index of the order status in the array
    return status_array[status]


