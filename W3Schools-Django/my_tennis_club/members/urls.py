from django.urls import path
from . import views

urlpatterns = [
    # Added path to make sure that root url points to main view
    path('', views.main, name='main'),
    
    # Path below makes sure that members url points to members view
    path('members/', views.members, name='members'),
    
    # "/details/ url points to correct details view with id as a parameter" 
    # <int:id> is a path converter that matches zero or a positive integer. 
    # In this case the positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # Also see stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat
    path('members/details/<int:id>', views.details, name='details'),
    
    # Add path to make sure that testing url (just for testing purposes) points to testing view
    path('testing/', views.testing, name='testing')
]