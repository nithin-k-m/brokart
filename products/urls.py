
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index,name='home'),#route to index view, when the user accesses the root URL of the application then this view function will be called and it will render the index.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    path('product_list/',views.list_products,name='list_product'),#route to product listing view, when the user accesses the /products URL of the application then this view function will be called and it will render the list_products.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    path('product_detail/',views.detail_product,name='detail_product')#route to product detail view, when the user accesses the /products/<id> URL of the application then this view function will be called and it will render the detail_product.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
]
