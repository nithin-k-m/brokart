from django.shortcuts import render

# Create your views here.
def show_account(request):# view function for handling the account page of the application, when the user accesses the /account URL of the application then this view function will be called and it will render the account.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    return render(request,'customers/account.html')#rendering the account.html template for the account page of the application, account.html is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'