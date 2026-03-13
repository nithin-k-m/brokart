from django.shortcuts import render,redirect
from django.contrib.auth.models import User# to import the User model from django.contrib.auth.models, we can use this User model to create a new user account for the user and log them in to the application, we can also use this User model to authenticate the user when they try to log in to the application
from django.contrib import messages# to import the messages module from django.contrib, we can use this messages module to display success or error messages in the account page of the application after creating a new user account for the user and logging them in to the application, we can use the messages.success() method to display a success message and messages.error() method to display an error message in the account page of the application
from django.contrib.auth import authenticate, login, logout# to import the authenticate, login and logout functions from django.contrib.auth, we can use these functions to authenticate the user when they try to log in to the application, log the user in to the application after creating a new user account for the user and log the user out of the application when they click on the logout button in the account page of the application 
from . models import Customers

def sign_out(request):
    logout(request)
    return redirect('account')

# Create your views here.
def show_account(request):# view function for handling the account page of the application, when the user accesses the /account URL of the application then this view function will be called and it will render the account.html template which is located in templates folder as we have specified the template directory in settings.py as BASE_DIR / 'templates'
    context={}
    error_message= None# to set the default value of error_message variable to None, we can use this error_message variable to store any error message that may occur while creating a new user account for the user and logging them in to the application, this error message will be displayed in the account page of the application using the context dictionary that we will pass to the template
    
    if request.POST and 'register' in request.POST:# checking if the request method is POST and if the register button is clicked, if both conditions are true then we need to get the values of username, password, email, address and phone_number parameters from the POST request, so that we can use these values to create a new user account for the user and log them in to the application
        context['register']=True# to set the value of 'register' key in context dictionary to True, this is to indicate that the user has clicked on the register button in the account page of the application, we can use this 'register' key in template to display the registration form in the account page of the application when the user clicks on the register button in the account page of the application
        try:# using try-except block to handle any exceptions that may occur while creating a new user account for the user and logging them in to the application, this is to prevent the application from crashing if there is any error while creating a new user account for the user and logging them in to the application    
            
            print(request.POST)# printing the POST request data to check if we are getting the values of username, password, email, address and phone_number parameters from the POST request correctly, this is for debugging purpose and we can remove this print statement after checking the POST request data
            username=request.POST.get('username')# getting the value of username parameter from the POST request, we can use this username variable to authenticate the user and log them in to the application
            password=request.POST.get('password')# getting the value of password parameter from the POST request, we can use this password variable to authenticate the user and log them in to the application
            email=request.POST.get('email')# getting the value of email parameter from the POST request, we can use this email variable to create a new user account for the user and log them in to the application
            address=request.POST.get('address')# getting the value of address parameter from the POST request, we can use this address variable to create a new user account for the user and log them in to the application
            phone=request.POST.get('phone')# getting the value of phone number parameter from the POST request, we can use this phone variable to create a new user account for the user and log them in to the application
        
            #creates user account 
            user = User.objects.create_user(name =username,
                                            username=username,
                                            password=password,
                                            email=email)# creating a new user account for the user using the create_user() method of User model and passing the values of username, password and email parameters that we have got from the POST request, we can use this user variable to log the user in to the application
        
            # creates customer account
            customer = Customers.objects.create(user=user,
                                                address=address,
                                                phone=phone)# creating a new customer account for the user using the create() method of Customers model and passing the values of user, address and phone parameters that we have got from the POST request, we can use this customer variable to log the user in to the application
            
            success_message="User registered successfully"# setting a success message to be displayed in the account page of the application after creating a new user account for the user and logging them in to the application, this success message will be displayed in the account page of the application using the context dictionary that we will pass to the template
            messages.success(request,success_message)# using the messages.success() method to display a success message in the account page of the application after creating a new user account for the user and logging them in to the application, we need to pass the request object and the success message as arguments to the messages.success() method to display the success message in the account page of the application
            
        except Exception as e:# using except block to catch any exceptions that may occur while creating a new user account for the user and logging them in to the application, this is to prevent the application from crashing if there is any error while creating a new user account for the user and logging them in to the application
           error_message="Duplicate username or invalid inputs"# setting an error message to be displayed in the account page of the application if there is any error while creating a new user account for the user and logging them in to the application, this error message will be displayed in the account page of the application using the context dictionary that we will pass to the template
           messages.error(request,error_message)# using the messages.error() method to display the error message in the account page of the application, we need to pass the request object and the error message as arguments to the messages.error() method to display the error message in the account page of the application
    
    if request.POST and 'login' in request.POST:# checking if the request method is POST and if the login button is clicked, if both conditions are true then we need to get the values of username and password parameters from the POST request, so that we can use these values to authenticate the user and log them in to the application
        context['register']=False# to set the value of 'login' key in context dictionary to True, this is to indicate that the user has clicked on the login button in the account page of the application, we can use this 'login' key in template to display the login form in the account page of the application when the user clicks on the login button in the account page of the application
       
       
        print(request.POST)# printing the POST request data to check if we are getting the values of username and password parameters from the POST request correctly, this is for debugging purpose and we can remove this print statement after checking the POST request data
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)# using the authenticate() function to authenticate the user with the given username and password, we need to pass the request
        if user:
            login(request, user)# using the login() function to log the user in to the application, we need to pass the request object and the user object that we have got from the authenticate() function as arguments to the login() function to log the user in to the application
            return redirect('home')# redirecting the user to the home page of the application after logging them in to the application, we need to pass the name of the URL pattern for the home page as an argument to the redirect() function to redirect the user to the home page of the application
        else:
            messages.error(request,'Invalid user credentials')# using the messages.error() method to display the error message in the account page of the application, we need to pass the request
    
    context['error_message']=error_message# adding the error_message variable to the context dictionary with the key 'error_message', so that we can access the error_message variable in template using the key 'error_message' to display the error message in the account page of the application if there is any error while creating a new user account for the user and logging them in to the application
    return render(request,'account.html',context)#rendering the account.html template for the account page of the application, account.html is located in templates folder as we have specifiedthe template directory in settings.py as BASE_DIR / 'templates'