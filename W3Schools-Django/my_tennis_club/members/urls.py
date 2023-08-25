# Original 2 imports below, created in URLs, within (9 Django URLs) of Django Tutorial Section
# are originally used with members url 
from django.urls import path
from . import views



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
    path('', views.main, name='main'),
    
    # URLs, within (9 Django URLs) of Django Tutorial Section
    # Original members path below makes sure that members url points to members view
    # Here 'members/' is url path, views.name a function_name (is members within views.py file)
    # and name has members as a url name. 
    path('members/', views.members, name='members'),
    
    # Add URLs, within Django Add Link to Details (17 Django - Add Link to Details ) of Django Display Data Section
    # Now we need to make sure that /details/ url points to correct details view, with id as a parameter.
    # Here # 'members/details/ part of url points to correct details view for a member.
    # # <int:id> is a path converter that matches zero or a positive integer, hence int.
    # In this case positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # and stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat 
    # Here views a function_name (is details within views.py file) and name has details in url name.
    # Note: url is members/details, so details name comes after members for a member.
    path('members/details/<int:id>', views.details, name='details'), 
    
    # URLs, within Django Add Test View (21 Django - Add Test View) of Django Display Data Section
    # When testing different aspects of Django, it can be a good idea to have somewhere to test code 
    # without destroying main project. URL path below is only used for testing purposes. 
    # We have to make sure that incoming urls to /testing/ will be redirected to testing view
    # Here 'testing/' is url path, views.testing a function_name (is testing within views.py file)
    # and name has testing as a url name. 
    path('testing/', views.testing, name='testing'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    # "/details/ url points to correct details view with id as a parameter" 
    # <int:id> is a path converter that matches zero or a positive integer. 
    # In this case the positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # Also see stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat
    path('members/details/<int:id>', views.details, name='details'),
    
    # Add path to make sure that testing url (just for testing purposes) points to testing view
    path('testing/', views.testing, name='testing')
]