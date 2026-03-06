from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [ 
    path('cart',views.show_cart,name='cart'),#route to cart view, when the user accesses the /cart URL of the application then this view function will be called and it will render the cart.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
]