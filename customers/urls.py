from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [ 
    path('account',views.show_account,name='account'),#route to account view, when the user accesses the /account URL of the application then this view function will be called and it will render the account.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    path('logout',views.sign_out,name='logout')#route to logout view, when the user accesses the /logout URL of the application then this view function will be called and it will log the user out of the application and redirect them to the account page of the application, we can use this logout view to log the user out of the application when they click on the logout button in the account page of the application
]