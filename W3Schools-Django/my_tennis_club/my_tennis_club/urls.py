"""
URL configuration for my_tennis_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# Imports below came with original setup of my_tennis_club project (except include)  
# , which was added in URLs part, within (9 Django URLs) of Django Tutorial Section
from django.contrib import admin
# Here we are using a django.contrib module for administration, to import an admin library for path() function below
from django.urls import include, path   
# Here we are using a django.urls module for urls, to import a path library for path() function below
# 


# This urlpatterns is a list that takes requests for urls
urlpatterns = [
    
    # Add members url in URLs part, within (9 Django URLs) of Django Tutorial Section
    # Here I am doing routing in my_tennis_club root directory my_tennis_club/my_tennis_club/urls.py , 
    # using a path function and include module. 
    # These have arguments, that will route users to members page, coming in via 127.0.0.1:8000/ localhost.
    path('', include('members.urls')),
    
    # I do not need to have a path for new first route for some reason. I need to research to find out why.
    #path('', first.urls),
    
    
    # This url path came with original setup of my_tennis_club project 
    path('admin/', admin.site.urls),
    # This url is used for administation login with Django.
    # The urlpatterns[] list takes requests going to admin/ and sends them to admin.site.urls, 
    # which is part of a built-in application that comes with Django. It contains a lot of functionality 
    # and user interfaces, one of them being the log-in user interface. 
    # This is mentioned in Getting Started, within (22 Django Admin) of Admin Section   
    # By default Django admin is enabled on all projects with path('admin/', admin.site.urls)
    # This path definition tells Django to enable admin site app on /admin/ url (eg http: //127.0.0.1:8000/admin/) 
    # see webforefront.com/django/setupdjangoadminsite.html, webforefront.com/django/setupdjangocontent.html
    # and tutorial.djangogirls.org/en/django_urls/ found from path('admin/' admin.site.urls) google search. 
    
]
