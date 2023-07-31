# Original 2 imports below, created in URLs, within (9 Django URLs) of Django Tutorial Section
# are originally used with members url 
from django.urls import path
from . import views


urlpatterns = [
    
    # Original members path created in URLs, within (9 Django URLs) of Django Tutorial Section
    # Path below makes sure that members url points to members view
    path('members/', views.members, name='members'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Added path to make sure that root url points to main view (Home Page)
    path('', views.main, name='main'),
    
    
    
    
    # "/details/ url points to correct details view with id as a parameter" 
    # <int:id> is a path converter that matches zero or a positive integer. 
    # In this case the positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # Also see stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat
    path('members/details/<int:id>', views.details, name='details'),
    
    # Add path to make sure that testing url (just for testing purposes) points to testing view
    path('testing/', views.testing, name='testing')
]