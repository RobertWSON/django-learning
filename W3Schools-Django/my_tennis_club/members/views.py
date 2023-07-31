# Below I am explaining what terms mean in this views.py file.
# This helps give me a better understanding on what the code is doing. 

# Imports 
# from django.shortcuts import render 
#  - Uses a django.shortcuts module to import a render library

# from django.http import HttpResponse 
# - Uses a django.http module to import an HttpResponse class

# from django.http import HttpResponse, HttpResponseRedirect
# - 

# from django.template import loader
# - 

# from .models import Member
# - 





# Original 2 imports below, created in Views, within (8 Django Views) of Django Tutorial Section 
from django.shortcuts import render
# import render library from django.shortcuts module.
# django.shortcuts is a module, that collects helper functions and classes that “span” multiple levels of MVC. 
# Check out another internet source educative.io/answers/how-to-render-data-in-django
# Django shortcuts installs a django binary library that proxies Django's manage.py and django-admin.py scripts
from django.http import HttpResponse
# HttpResponse is a class that lives in django.http module, so it is imported here   


# Create your views here.
 
# Original members view created in Views, within (8 Django Views) of Django Tutorial Section
def members(request):
#    {# This displays just Hello world! on localhost 127.0.0.1:8000/members/ in next Django URLs part #}
    return HttpResponse("Hello world!") 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# Modify the View within (10 Django Templates) under Django Tutorial Section    
#def members(request) 
#   {# HTML Template to be used with loader #}     
#   template = loader.get_template('myfirst.html') 
#   {# Modify HttpResponse with Template for rendering web page #}   
#   return HttpResponse(template.render())
#   {# This displays Hello World! as a heading with Welcome to my first Django project! underneath as a paragraph 
#    on localhost 127.0.0.1:8000/members #} 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 #, HttpResponseRedirect
# Use loader to Modify web page view
#from django.template import loader
# import Member Model, so we can use it display info from its Table  
#from .models import Member
 
 
 
 

# View that makes member model data in members folder, available from a template
#def members(request):
    # Add this to create an object with all values of Member model to update Member Table
#    mymembers = Member.objects.all().values()   
    # HTML Template to be used with loader
    # template = loader.get_template('myfirst.html')
    # Now load all_members.html template instead of myfirst.html
#    template = loader.get_template('all_members.html')
    # Create object containing mymembers object
#    context = {
#        'mymembers': mymembers,   
        # mymembers here, relates to all people (members) for the list taken from ids in a table.  
#    }
    # return HttpResponse("Hello world!")
    # Modify HttpResponse with Template for rendering web page 
    # return HttpResponse(template.render()) 
    # Now change to send object to template and output HTML rendered by template
#    return HttpResponse(template.render(context, request))

# View for dealing with incoming requests from /details/ url
#def details(request, id):
    # Get id as an argument and use it to locate correct record in Member Table. 
#    mymember = Member.objects.get(id=id)
    # HTML details template to be used with loader
#    template = loader.get_template('details.html')
#    # Creates an object containing a member
#    context = {     # mymember string relates to a property name for example phone or joined_date.
                    # This is taken from one person's details, eg from an id in a table.
#        'mymember': mymember,  
        # mymember here, relates to a property value of that property name. 
#    }
    # Sends object to template and output HTML rendered by template. W3Schools does not use id for rendering
#    return HttpResponse(template.render(context, request))

# View for dealing with incoming requests to root / of the project (main home landing page)
#def main(request):
    # HTML main Template to be used with loader (Load main html template)
#    template = loader.get_template('main.html')
    # Output HTML that is rendered by template. W3Schools does not include request with render for some reason.
#    return HttpResponse(template.render())

# View for dealing with testing different aspects of Django, 
# as it can be a good idea to have somewhere to test code without destroying main project.
# The View can deal with incoming rquests from a /testing/ url, to see how the testing works.  
#def testing(request):
    # HTML Template to be used with loader (load Template html file)
#    template = loader.get_template('template.html')
    # Creates an object containing fruits as an array
    #context = {       # fruits is the object name  
    # 'fruits': ['Apple', 'Banana', 'Cherry'],  # fruits object is an Array that has a variety of fruits   
    #'firstname': 'Linus' , # HTMLTemplate Variable is given a name here
#}
# Sends object to template and output HTML rendered by template. 
# return HttpResponse(template.render(context, request))

# Use return Below for Creating Variables in Template within Django Variable of Django Syntax Section 
#    return HttpResponse(template.render()) 
# Does not need request with HttpResponse (I am not completely sure why this is at the moment)
# See docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
# Views within (8 Django Views) of Django Tutorial Section
#def members(request):
#    {# This displays just Hello world! on localhost 127.0.0.1:8000/members/ in next Django URLs part #}
#    return HttpResponse("Hello world!")     
      
      
      
# Modify the View within (10 Django Templates) under Django Tutorial Section    
#def members(request) 
#   {# HTML Template to be used with loader #}     
#   template = loader.get_template('myfirst.html') 
#   {# Modify HttpResponse with Template for rendering web page #}   
#   return HttpResponse(template.render())
#   {# This displays Hello World! as a heading with Welcome to my first Django project! underneath as a paragraph 
#    on localhost 127.0.0.1:8000/members #}
        
            


# Data from a Model within Django Variable of Django Syntax Section    
#def testing(request):
#    mymembers = Member.objects.all().values()    
#    template = loader.get_template('template.html')
#    context = {
#        'mymembers': mymembers,
#    }
#    return HttpResponse(template.render(context, request))
    
    
    
# Django Template Tags within Django Tags of Django Syntax Section
#def testing(request):
#    template = loader.get_template('template.html')
#    context = {
#    'greeting': 1,
#    }
#    return HttpResponse(template.render(context, request))



# Django Code within Django Template Tags (30 Django Tags) of Django Syntax Section 
#def members(request):
    # Add this to create an object with all values of Member model to update Member Table
#    mymembers = Member.objects.all().values()   
    # HTML Template to be used with loader
    # template = loader.get_template('myfirst.html')
    # Now load all_members.html template instead of myfirst.html
#    template = loader.get_template('all_members.html')
    # Create object containing mymembers object
#    context = {
#        'mymembers': mymembers,   
        # mymembers here, relates to all people (members) for the list taken from ids in a table.  
#    }




# Test Template within Django Add Test View (21 Django - Add Test View) of Django Display Data Section #}    
#def testing(request)      
#    template = loader.get_template('template.html')
#    context = {
#    'fruits': ['Apple', 'Banana', 'Cherry'],  # fruits object is an Array that has a variety of fruits   
#    }
#    Sends object to template and output HTML rendered by template. 
#    return HttpResponse(template.render(context, request))



# If Statement within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_tmeplate('template.html')
#   context = {
#       'greeting': 1,     
#   }
#   return HttpResponse(template.render(context, request))


# Elif within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#    'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# Else within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 3,      
#   }
#   return HttpResponse(template.render(context, request))


# Operators within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 2,      
#   }
#   return HttpResponse(template.render(context, request))


# == within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 2,      
#   }
#   return HttpResponse(template.render(context, request))


# != within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 2,      
#   }
#   return HttpResponse(template.render(context, request))


# < within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# <= within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# > within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# >= within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# and within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For and operator, we have 2 variables below, that can be used in template.html 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 1,
#     'day': 'Friday',    
#   }
#   return HttpResponse(template.render(context, request))


# or within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For or operator, we have 1 variable with an initial value below, that can be used in template.html
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 1,   
#   }
#   return HttpResponse(template.render(context, request))


# and/or within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For and/or operator, we have 2 variables below, that can be used in template.html
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'greeting': 5,
#     'day': 'Friday',    
#   }
#   return HttpResponse(template.render(context, request))


# in within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For in operator, we have 1 array variable below that can be used in template.html.
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #} 
#def testing(request):
#   template = loader.get_template('template.html')
# {# Context Creates an object containing a fruits property and an array with fruit values #}
#   context = {
#      'fruits': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))


# not in within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For not in operator, we have 1 array variable below that can be used in template.html.
# Up top it uses {# from django.http import HttpResponse #}
#               {# from django.template import loader #} 
#def testing(request):
# {# Context Creates an object containing a fruits property and an array with fruit values #}
#   context = {
#      'fruits': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))


# is within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For is operator, we have 2 array variables (recognized as objects) below, that can be seen if they  
# have same identity or not in template.html.
# Up top it uses {# from django.http import HttpResponse #}
#               {# from django.template import loader #}
#def testing(request):
# {# Context Creates 2 objects as x and y variables, that work as properties and each property  
#   has an array with values. #}
#   context = {
#      'x': ['Apple', 'Banana', 'Cherry'],
#      'y': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))


# replace is with ==  within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For == instead of is operator, we have 2 variables below that can be seen if they have same values  
# or not in template.html  
# Up top it uses {# from django.http import HttpResponse #}
#               {# from django.template import loader #}
#def testing(request):
# {# Context Creates 2 objects as x and y variables, that work as properties and each property  
#   has an array with values. #}
#   context = {
#      'x': ['Apple', 'Banana', 'Cherry'],
#      'y': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))

  
# with and is within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section 
# Using with and is, we have 2 objects pointing to same object (Variable) and we are seeing if they 
# have same identity or not in template.html.
# Up top it uses {# from django.http import HttpResponse #}
#               {# from django.template import loader #}
#def testing(request):
# {# Context Creates 2 objects as x and y variables, that work as properties and each property  
#   has an array with values. #}
#   context = {
#      'x': ['Apple', 'Banana', 'Cherry'],
#      'y': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))


# is not within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For is not operator, we are checking if 2 objects are the same or not, 
# through their identy in template.html. 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
# {# Context Creates 2 objects as x and y variables, that work as properties and each property  
#   has an array with values. #}
#   context = {
#      'x': ['Apple', 'Banana', 'Cherry'],
#      'y': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))


# For Loop List within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section 
# We are using fruits object and each of its items within an array for template.html. 
# Up top it uses {# from django.http import HttpResponse #}
#                 {# from django.template import loader #}
#def testing(request):
# {# Context Creates 1 object, a fruits variable, that works as properties and each property  
#    has an array with values. #}
#   context = {
#      'fruits': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))

# For Loop Dictionaries within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section 
# We are using cars object, which has properties and property values within it, that can be used in template.html
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):
# {# Context Creates 1 cars object, that has an array with groups (dictionaries) of properties 
#    and property values for each car. #}
#   context = {
#     'cars': [
#        {
#          'brand': 'Ford',
#          'model': 'Mustang',
#          'year': '1964',
#        },
#        {
#          'brand': 'Ford',
#          'model': 'Bronco',
#          'year': '1970',
#        },
#        {
#          'brand': 'Volvo',
#          'model': 'P1800',
#          'year': '1964',
#        }]     
#     } 
#   return HttpResponse(template.render(context, request))



# Data from a Model within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section
# We are using members object, which has properties and property values within it, #}
# that can be used in numerical id order within template.html
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#                {# from .models import Member #}
#def testing(request):
# {# Add this below to create an object with all values of Member model to update Member Table #}
#  mymembers = Member.objects.all().values()
#  template = loader.get_template('template.html')
#  {# Context creates a members object that has a property name of mymembers with a value. #}
#  context = {
#    'members': mymembers,   
#  }
#  return HttpResponse(template.render(context, request))



# Reversed within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section
# We are using members object, which has properties and property values within it,
# that can be used in numerical id order within template.html
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#                {# from .models import Member #}
#def testing(request):
# {# Add this below to create an object with all values of Member model to update Member Table #}
#  mymembers = Member.objects.all().values()
#  template = loader.get_template('template.html')
#  {# Context creates a members object that has a property name of mymembers with a value. #}
#  context = {
#    'members': mymembers,   
#  }
#  return HttpResponse(template.render(context, request))



# Empty within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #}
# We are using emptytestobject, which has an empty array with no property, 
# that can be used in template.html
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates an emptytestobject object that has an array, but it has no values, so it is empty. #}
#  context = {
#    'emptytestobject': [],   
#  }
#  return HttpResponse(template.render(context, request))


# Empty used if object does not exist, 
# within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section  
# We are using fruits object here, but it is non existant in template.html, 
# as an object that has a different name is used there. 
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates a fruits object that has an array with property values, #}
#  {# but this object is not used in template.html . #}
#  context = {
#    'emptytestobject': [],   
#  }
#  return HttpResponse(template.render(context, request))



# Django has some variables that are available for you inside a loop:
# We cover these forloop variables below. 

# forloop.counter within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #}
# We are using indexes of an array here from fruits object, so it can be displayed in template.html.
# forloop.counter allows us to display array indexes in order, from 1 up top, to 5 down bottom of list on a page.
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# However instead of array values, we are using array indexes, #}
#  {# for example apple has an index of 1 and Kiwi has an index of 5 in array. #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))



# forloop.counter0 within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #}
# We are using indexes of an array here from fruits object, so it can be displayed in template.html.
# forloop.counter0 allows us to display array indexes in order, from 0 up top, to 4 down bottom of list on a page
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# However instead of array values, we are using array indexes with counter0, #}
#  {# for example apple has an index of 0 and Kiwi has an index of 4 in this array. #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))



# forloop.first within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #}
# We are using array values here from fruits object, so it can be displayed in template.html.
# forloop.first allows us to highlight first index value from array below 
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# These array values will be displayed in a list and the first value Apple will be highlighted #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))



# forloop.last within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #}
# We are using array values here from fruits object, so it can be displayed in template.html.
# forloop.last allows us to highlight last index value from array below 
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# These array values will be displayed in a list and the last value Kiwi will be highlighted #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))



# forloop.revcounter within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #} 
# We are using indexes of an array here from fruits object, so it can be displayed in template.html.
# forloop.revcounter allows us to display array indexes in reverse order, from 5 up top, to 1 down bottom of list on a page
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# However instead of array values, we are using array indexes. #}
#  {# Kiwi has an index of 5 in array below and will be displayed at top of list on page. #}
#  {# Apple has an index of 1 and will be displayed at bottom of list on page. #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))



# forloop.revcounter0 within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #} 
# We are using indexes of an array here from fruits object, so it can be displayed in template.html.
# forloop.revcounter0 allows us to display array indexes in reverse order, from 4 up top, to 0 down bottom of list on a page
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request):
#  template = loader.get_template('template.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# However instead of array values, we are using array indexes in reverse order for revcounter0. #}
#  {# Kiwi has an index of 4 in array below and will be displayed at top of list on page. #}
#  {# Apple has an index of 0 and will be displayed at bottom of list on page. #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))