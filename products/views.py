from urllib import request
from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):# view function for handling the index page of the application, when the user accesses the root URL of the application then this view function will be called and it will render the index.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    featured_product= Product.objects.order_by('priority')[:4]# fetching the top 4 products from the database using objects.order_by() method of Product model and slicing it to get the top 4 products and storing it in featured_product variable, we can pass this featured_product variable to template to display the featured products in the index page of the application
    latest_products= Product.objects.order_by('-id')[:8]# fetching the latest 4 products from the database using objects.order_by() method of Product model and slicing it to get the latest 4 products and storing it in latest_product variable, we can pass this latest
    context={
        'featured_product':featured_product,
             'latest_products':latest_products
             }#creating a context dictionary to pass the featured_product and latest_product variables to template with the keys 'featured_product' and 'latest_products', so that we can access the featured_product and latest_products variables in template using the keys 'featured_product' and 'latest_products'
    print(context)# printing the context dictionary to check if the featured_product and latest_product variables are being passed to template correctly, this is for debugging purpose and we can remove this print statement after checking the context dictionary
    return render(request,'index.html',context)#rendering the index.html template for the index page of the application, index.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'

def list_products(request):# view function for handling the product listing page of the application, when the user accesses the /products URL of the application then this view function will be called and it will render the list_products.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    """_summary_
    returns product listing page of the application, when the user accesses the /products URL of the application then this view function will be called and it will render the list_products.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page=1# to set the default page number to 1, we can use this page variable to get the products for the current page and pass it to template to display the products for the current page in the product listing page of the application
    if request.GET:# checking if there are any query parameters in the URL, if there are then we need to get the value of page parameter from the URL query parameters and set it to page variable, so that we can use this page variable to get the products for the current page and pass it to template to display the products for the current page in the product listing page of the application
        page=request.GET.get('page',1)# getting the value of page parameter from the URL query parameters, if the page parameter is not present in the URL then it will return 1 as default value, we can use this page variable to get the products for the current page and pass it to template to display the products for the current page in the product listing page of the application
    product_list= Product.objects.order_by('priority')#fetching all the products from the database using objects.all() method of Product model and storing it in product_list variable, we can use this product_list variable to get the products for the current page and pass it to template to display the products for the current page in the product listing page of the application
    product_paginator = Paginator(product_list,2)# creating a Paginator object with product_list and number of products to be displayed per page(2 in this case), we can use this product_paginator object to get the products for the current page and pass it to template to display the products for the current page in the product listing page of the application
    product_list = product_paginator.get_page(page)# getting the products for the current page using get_page() method of Paginator object and storing it in product_list variable, we can pass this product_list variable to template to display the products for the current page in the product listing page of the application
    context={'products':product_list}#creating a context dictionary to pass the product_list variable to template with the key 'products', so that we can access the product_list variable in template using the key 'products'
    return render(request,'products.html',context)#rendering the products.html and context template for the product listing page of the application, list_products.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'


def detail_product(request,pk):# view function for handling the product detail page of the application, when the user accesses the /products/<id> URL of the application then this view function will be called and it will render the detail_product.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    product = Product.objects.get(pk=pk)# fetching the product with the given primary key (pk) from the database using objects.get() method of Product model and storing it in product variable, we can pass this product variable to template to display the details of the product in the product detail page of the application
    context={'product':product}#creating a context dictionary to pass the product
    return render(request,'product_details.html',context)#rendering the product_detail.html template for the product detail page of the application, detail_product.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'








