from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):# view function for handling the index page of the application, when the user accesses the root URL of the application then this view function will be called and it will render the index.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    return render(request,'index.html')#rendering the index.html template for the index page of the application, index.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'

def list_products(request):# view function for handling the product listing page of the application, when the user accesses the /products URL of the application then this view function will be called and it will render the list_products.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    """_summary_
    returns product listing page of the application, when the user accesses the /products URL of the application then this view function will be called and it will render the list_products.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request,'products.html')#rendering the products.html template for the product listing page of the application, list_products.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'


def detail_product(request):# view function for handling the product detail page of the application, when the user accesses the /products/<id> URL of the application then this view function will be called and it will render the detail_product.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    return render(request,'product_details.html')#rendering the product_detail.html template for the product detail page of the application, detail_product.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'








