# Original 2 imports below, created in URLs, within (9 Django URLs) of Django Tutorial Section
# are originally used with members url 
# Note: URL is a Uniform Resource Locator, used for web addresses
from django.urls import path
# Here we are using a django.urls module for urls, to import a path library for path() function below
# see fulstackpython.com/django-urls-path-examples.html, javatpoint.com/django-url-mapping
# and blog.devgenius.io/django-urls-d59f38b6e3cb
from . import views
# Here . (single dot) is a convention from command line applications. 
# Single dot means current directory (or module/package) of file that is used to get what we need.
# Imports that use this single dot ( . ) syntax are called relative imports.
# in this case views file (views.py) is in same directory (folder) as this urls.py file, so we use a dot. 
# We are using views.py as a relative import to get what we need for url routes.   
# see stackoverflow.com/questions/44262586/django-tutorial-from-import-views
# found from "from django from . import views" google search


urlpatterns = [
    
    # To help understand path functions in urlpatterns I have found a website.
    # From https://www.meetgor.com/django-basics-views-urls/ , breaking down path function in URLpatterns,
    # it shows that '' is url path, views is a function_name (with . showing that view is within views.py file
    # and in same directory as urls.py) and name is a url name.
    
    # Add URL, within Django Add Main Index Page (19 Django - Add Main Index Page) of Django Display Data Section 
    # Now we need to make sure that root url points to correct main view (for Home Page).
    # Add a path to make sure that root url (for Home Page) points to main view. 
    # Here '' is root url path for home page, views.main a function_name (is main within views.py file)
    # and because url does not have a name in it eg '', we have decided to give it main as a name.
    
    # comment code for now  
    path('', views.main, name='main'),
    
    # URLs, within (9 Django URLs) of Django Tutorial Section
    # Original members path below makes sure that members url points to members view
    # Here 'members/' is url path, views.name a function_name (is members within views.py file)
    # and name has members as a url name. 
    
    
    # Add a hello path for a url that will is used for displaying just Hello World!
    # Note: I do not need name='first' for this tour for some reason. I need to research to find out why. 
    path('hello/', views.hello, name='hello'),
    
    
    # Add a first path for a url that will be used for displaying Hello World! 
    # and Welcome to my first Django project! below. I think this is a better way to approach as it keeps
    # members separate.
    # Note: I do not need name='first' for this tour for some reason. I need to research to find out why.
    path('first/', views.first, name='first'),
    
    
    
    # comment code for now    
    path('members/', views.members, name='members'),
    
    # Add URLs, within Django Add Link to Details (17 Django - Add Link to Details ) of Django Display Data Section
    # Now we need to make sure that /details/ url points to correct details view, with id as a parameter.
    # Here # 'members/details/ part of url points to correct details view for a member.
    # # <int:id> is a path converter that matches zero or a positive integer, hence int.
    # In this case positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # and stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat 
    # Here views a function_name (is details within views.py file) and name has details in url name.
    # Note: url is members/details, so details name comes after members for a member.
    
    # comment code for now  
    path('members/details/<int:id>', views.details, name='details'), 
    
    
    # URLs, within Django Add Test View (21 Django - Add Test View) of Django Display Data Section
    # When testing different aspects of Django, it can be a good idea to have somewhere to test code 
    # without destroying main project. URL path below is only used for testing purposes. 
    # We have to make sure that incoming urls to /testing/ will be redirected to testing view
    # Here 'testing/' is url path, views.testing a function_name (is testing within views.py file)
    # and name has testing as a url name. 
   
    
    # comment code for now
     # Add path to make sure that testing url (just for testing purposes) points to testing view
    #path('testing/', views.testing, name='testing') 
    path('testing/', views.testing, name='testing'),
    
    
    
    
    # I do not need path code for this below, but I may need description for understanding on what these paths do. 
    # , so I will Comment it out for now. 
    
    # "/details/ url points to correct details view with id as a parameter" 
    # <int:id> is a path converter that matches zero or a positive integer. 
    # In this case the positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # Also see stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat
    #path('members/details/<int:id>', views.details, name='details'),
    
   
    
    
    # Add Routes for Django References Section
    # Template Tag Reference 
    path('template/', views.template, name='template'),
    
    # Filter Reference
    path('filter/', views.filter, name='filter'),
    
    # Field Lookups Reference
    path('field/', views.field, name='field'),
]