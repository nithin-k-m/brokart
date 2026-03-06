from django.shortcuts import render

# Create your views here.
def show_cart(request):# view function for handling the cart page of the application, when the user accesses the /cart URL of the application then this view function will be called and it will render the cart.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    return render(request,'cart.html')#rendering the cart.html template for the cart page of the application, cart.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'

