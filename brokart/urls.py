"""
URL configuration for brokart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),#route to admin site
    path('',include('products.urls'))#including the urls of products app, when the user accesses the root URL of the application then it will look for the urls in products app and route accordingly

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#to serve media files through django server in debug mode, this line will only work if DEBUG is True in settings.py