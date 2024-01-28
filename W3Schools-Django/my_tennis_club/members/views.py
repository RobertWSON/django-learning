# Below I am explaining what terms mean in this views.py file.
# This helps give me a better understanding on what the code is doing. 

# Imports 
# from django.shortcuts import render 
#  - Uses a django.shortcuts module to import a render library
#    django.shortcuts module is used for  
#    render is used for render() function with templates, requests etc. 
#    See javatpoint.com/django-shortcuts and educative.io/ansers/how-to-render-data-in-django


# from django.http import HttpResponse 
# - Uses a django.http module to import an HttpResponse class from a library
#   django.http module is used for  
#   HttpResponse is a class used for HttpResponse() function for displaying text on a page. 
#    See pytutorial.com/fjango-httpresponse/


# from django.http import HttpResponse, HttpResponseRedirect
# - 

# from django.template import loader
# - 

# from .models import Member
# - 

  

# Create your views here.

 
# Views within (8 Django Views) of Django Tutorial Section 
 # Original 2 imports below, created in Views, within (8 Django Views) of Django Tutorial Section 
 
# comment code for now   from django.shortcuts import render

# import render library from django.shortcuts module.
# django.shortcuts is a module, that collects helper functions and classes that “span” multiple levels of MVC. 
# Check out another internet source educative.io/answers/how-to-render-data-in-django
# Django shortcuts installs a django binary library that proxies Django's manage.py and django-admin.py scripts

# comment code for now   
from django.http import HttpResponse
#from django.http import HttpResponseRedirect
# HttpResponse is a class that lives in django.http module, so it is imported here 
from django.template import loader
# loader is a class that is in django.template module and is used for loading data from a template
from .models import Member

 
# Original members view created in Views, within (8 Django Views) of Django Tutorial Section

# comment code for now   def members(request):
# I have now decided to have my own view called first. 
# Having my own view allows me to separate this page from members page, which requires use of database.
# I feel that this the best way to approach this
def hello(request):

#    {# This displays just Hello world! on localhost 127.0.0.1:8000/members/ in next Django URLs part #}
    # comment code for now   
    return HttpResponse("Hello world!") 
 
  
 
# Modify the View within Django Templates (10 Django Templates) under Django Tutorial Section 
#from django.http import HttpResponse
#from django.template import loader
#from .models import Member
   
#def members(request):
# I have now decided to have my own view called first. 
# Having my own view allows me to separate this page from members page, which requires use of database.
# I feel that this the best way to approach this 
#def first(request): 

#I have found that first is also used in Django Reference Section for templates,
#so I have to give this a different name
def first_django_page(request):
#   {# HTML Template to be used with loader #}     
   template = loader.get_template('myfirst.html') 
#   {# Modify HttpResponse with Template for rendering web page #}   
   return HttpResponse(template.render())
    # This displays Hello World! as a heading with Welcome to my first Django project! underneath, 
    # as a paragraph on localhost 127.0.0.1:8000/members  
 
 
 
# Create a view for handling Prepare Template and View Page. This will be for testing//prepare_template url  
# and Django Prepare Template (16 Prepare Template & View) of Display Data Section.
 
# These imports below are used above at top of views.py 
#from django.http import HttpResponse
#from django.template import loader
def prepare_template(request): 
  template = loader.get_template('testing/template_and_view.html')
  return HttpResponse(template.render())
 
# Modify View within Django Prepare Template (16 Prepare Template & View) of Display Data Section
# Comment this for now and use imports above from previous view in 10 Django Templates.
#from django.http import HttpResponse
#from django.template import loader
#from .models import Member

# View that makes member model data in members folder, available from a template

def members(request):
    # Add this to create an object with all values of Member model to update Member Table
    mymembers = Member.objects.all().values() 
    # HTML Template to be used with loader  
    # Now load all_members.html template instead of myfirst.html
    template = loader.get_template('all_members.html')
    # Create object containing mymembers object
    context = {
        'mymembers': mymembers,   
        # mymembers here, relates to all people (members) for the list taken from ids in a table.  
    }
    # return HttpResponse("Hello world!")
    # Modify HttpResponse with Template for rendering web page 
    # return HttpResponse(template.render()) 
    # Now change to send object to template and output HTML rendered by template
    #return HttpResponse(template.render(context, request))
  # Try no request with HttpResponse
    return HttpResponse(template.render(context, request))  


# Create new View within Django Add Link to Details (17 Django - Add Link to Details) of Display Data Section

#from django.http import HttpResponse
#from django.template import loader
#from .models import Member

# View for dealing with incoming requests from /details/ url
def details(request, id):
    # Get id as an argument and use it to locate correct record in Member Table. 
    mymember = Member.objects.get(id=id)
    # HTML details template to be used with loader
    template = loader.get_template('details.html')
#    # Creates an object containing a member
    context = {     # mymember string relates to a property name for example phone or joined_date.
                    # This is taken from one person's details, eg from an id in a table.
        'mymember': mymember,  
        # mymember here, relates to a property value of that property name. 
    }
    # Sends object to template and output HTML rendered by template. W3Schools does not use id for rendering
    return HttpResponse(template.render(context, request))




# Create new View within Django Add Main Index Page (19 Django - Add Main Index Page) of Display Data Section 
# View for dealing with incoming requests to root / of the project (main home landing page)
#from django.http import HttpResponse
#from django.template import loader
#from .models import Member

# This view is used for members page (/all_members.html url), which has all_members.html template
#def members(request):
  #mymembers = Member.objects.all().values()
  #template = loader.get_template('all_members.html')
  #context = {
    #'mymembers': mymembers,
  #}
  #return HttpResponse(template.render(context, request))


# This view is used for details page (/details.html url), which has details.html template
#def details(request, id):
  #mymember = Member.objects.get(id=id)
  #template = loader.get_template('details.html')
  #context = {
    #'mymember': mymember,
  #}
  #return HttpResponse(template.render(context, request))

# This view is used for main home page (/ url), which has main.html template 
def main(request):
    # HTML main Template to be used with loader (Load main html template)
    template = loader.get_template('main.html')
    # Output HTML that is rendered by template. W3Schools does not include request with render for some reason.
    return HttpResponse(template.render()) 




# Test Template within Django Add Test View (21 Add Test View) of Django Display Data Section #}

#from django.http import HttpResponse
#from django.template import loader
    
# I will now do this differently and use this example later on in 
# "For Loop List within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section". 
   
#def testing(request)      
#    template = loader.get_template('template.html')
#    context = {
#    'fruits': ['Apple', 'Banana', 'Cherry'],  # fruits object is an Array that has a variety of fruits   
#    }
#    Sends object to template and output HTML rendered by template. 
#    return HttpResponse(template.render(context, request))

# I have decided that testing view should be used for displaying a Django Examples page with links to each example.  
# template.html for this will be in testing folder.

#2 Imports below are used above on lines 44 to 46 
#from django.http import HttpResponse
#from django.template import loader

def testing(request):
   template = loader.get_template('testing/template.html')
   return HttpResponse(template.render())



# Add View within Django Add Test View (21 Django - Add Test View) of Django Display Data Section
# View for dealing with testing different aspects of Django, 
# as it can be a good idea to have somewhere to test code without destroying main project.
# The View can deal with incoming rquests from a /testing/ url, to see how the testing works. 
#from django.http import HttpResponse
#from django.template import loader
#from .models import Member
 
#def testing(request):
    # HTML Template to be used with loader (load Template html file)
#    template = loader.get_template('template.html')
    # Creates an object containing fruits as an array
    #context = {       # fruits is the object name  
    # 'fruits': ['Apple', 'Banana', 'Cherry'],  # fruits object is an Array that has a variety of fruits 
    #} 
    # Sends object to template and output HTML rendered by template. 
    #return HttpResponse(template.render(context, request))
     
     

# Create Variable in View within Django Template Variables (29 Django Syntax - Variables) 
# of Django Display Data Section    
    # firstname Linus is from Template Variables within Django Template Variables (29 Django Syntax - Variables)
    # of Django Syntax Section  
    #'firstname': 'Linus' , # HTML Template Variable is given a name here

#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
  #template = loader.get_template('template.html')
  #context = {
    #'firstname': 'Linus',  # HTML Template Variable is given a name here
  #}
  #return HttpResponse(template.render(context, request))



# Create Variables in Template within Django Variables (29 Django Syntax - Variables) 
# of Django Display Data Section
#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
    #template = loader.get_template('template.html')
# Use return Below for Creating Variables in Template within Django Variable of Django Syntax Section 
#    return HttpResponse(template.render()) 
# Does not need request with HttpResponse (I am not completely sure why this is at the moment)
# See docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects
      
      
      
      
      
# HttpResponseRedirect was introduced in Data From a Model, within Django Template Variables
# (29 Django Syntax - Variables) of Django Syntax Section)
 #, HttpResponseRedirect
# Use loader to Modify web page view
#from django.template import loader
# import Member Model, so we can use it display info from its Table  
#from .models import Member
        
            
# Data from a Model within Django Variable (29 Django Variables) of Django Syntax Section

#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
#from .models import Member
    
#def testing(request):
#    mymembers = Member.objects.all().values()    
#    template = loader.get_template('template.html')
#    context = {
#        'mymembers': mymembers,
#    }
#    return HttpResponse(template.render(context, request))
    
    
    
# Django Template Tags within Django Tags (30 Django Syntax - Tags) of Django Syntax Section

#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
#    template = loader.get_template('template.html')
#    context = {
#    'greeting': 1,
#    }
#    return HttpResponse(template.render(context, request))
def tags_tested(request):
  template = loader.get_template('testing/tags_tested.html')
  context = {
    'greeting': 1,
  }    
  return HttpResponse(template.render(context, request))
  
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
#from django.http import HttpResponse, HttpResponseRedirect
#from django.http import HttpResponseRedirect

#def django_code(request):
    # Add this to create an object with all values of Member model to update Member Table
  #mymembers = Member.objects.all().values()   
    # HTML Template to be used with loader
  #template = loader.get_template('testing/django_code.html')
    # Now load all_members.html template instead of myfirst.html
#    template = loader.get_template('all_members.html')
    # Create object containing mymembers object
  #context = {
    #'mymembers': mymembers,   
    # mymembers here, relates to all people (members) for the list taken from ids in a table.  
  #}
  #return HttpResponse(template.render(context, request))


# If Statement within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
def if_tested(request):
#   template = loader.get_template('template.html') Now use template below
  template = loader.get_template('testing/if_tested.html')
  context = {
    'greeting': 1,     
  }
  return HttpResponse(template.render(context, request))


# Elif within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_elif(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_elif.html')
#   context = {
#    'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# Else within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_else(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_else.html')
#   context = {
#     'greeting': 3,      
#   }
#   return HttpResponse(template.render(context, request))


# Operators within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_drop_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_drop_operator.html')
#   context = {
#     'greeting': 2,      
#   }
#   return HttpResponse(template.render(context, request))


# == within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_==_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_==_operator.html')
#   context = {
#     'greeting': 2,      
#   }
#   return HttpResponse(template.render(context, request))


# != within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_!=_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_!=_operator.html')
#   context = {
#     'greeting': 2,      
#   }
#   return HttpResponse(template.render(context, request))


# < within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_<_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_<_operator.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# <= within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_<=_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_<=_operator.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# > within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_>_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_>_operator.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# >= within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_>=_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_>=_operator.html')
#   context = {
#     'greeting': 2,
#   }
#   return HttpResponse(template.render(context, request))


# and within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For and operator, we have 2 variables below, that can be used in template.html 
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_and_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_and_operator.html')
#   context = {
#     'greeting': 1,
#     'day': 'Friday',    
#   }
#   return HttpResponse(template.render(context, request))


# or within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For or operator, we have 1 variable with an initial value below, that can be used in template.html
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_or_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_or_operator.html')
#   context = {
#     'greeting': 1,   
#   }
#   return HttpResponse(template.render(context, request))


# and/or within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For and/or operator, we have 2 variables below, that can be used in template.html
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_and-or_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_and-or_operator.html')
#   context = {
#     'greeting': 5,
#     'day': 'Friday',    
#   }
#   return HttpResponse(template.render(context, request))


# in within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For in operator, we have 1 array variable below that can be used in template.html.
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #} 
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_in_operator(request):
#   template = loader.get_template('template.html')
#   template = loader.get_template('testing/if_in_operator.html')
# {# Context Creates an object containing a fruits property and an array with fruit values #}
#   context = {
#      'fruits': ['Apple', 'Banana', 'Cherry'],
#   } 
#   return HttpResponse(template.render(context, request))


# not in within Django if Tag (31 Django Syntax - If Else) of Django Syntax Section
# For not in operator, we have 1 array variable below that can be used in template.html.
# Up top it uses {# from django.http import HttpResponse #}
#               {# from django.template import loader #} 
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_not-in_operator(request):
#   template = loader.get_template('testing/if_not-in_operator.html')
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
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def if_is-not_operator(request):
#   template = loader.get_template('testing/if_not-in_operator.html')
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
#def testing(request):  This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples. 
def for_loop_tested(request):
  template = loader.get_template('testing/for_loop_tested.html')
#  {# Context Creates 1 object, a fruits variable, that works as properties and each property  
#     has an array with values. #}
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

# For Loop Dictionaries within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section 
# We are using cars object, which has properties and property values within it, that can be used in template.html
# Up top it uses {# from django.http import HttpResponse #}
#                {# from django.template import loader #}
#def testing(request):  This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
def for_loop_dict(request):
  template = loader.get_template('testing/for_loop_dict.html')
# {# Context Creates 1 cars object, that has an array with groups (dictionaries) of properties 
#    and property values for each car. #}
  context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }]     
    } 
  return HttpResponse(template.render(context, request))


# Data from a Model within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section
# We are using members object, which has properties and property values within it, #}
# that can be used in numerical id order within template.html
# Up top it uses {# 
#from django.http import HttpResponse 
# , HttpResponseRedirect #} 
#                {# 
#from django.template import loader #}
#                {# from .models import Member #}

#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
def for_loop_modeldata(request):
# {# Add this below to create an object with all values of Member model to update Member Table #}
  mymembers = Member.objects.all().values()
#  template = loader.get_template('template.html')
  template = loader.get_template('testing/for_loop_modeldata.html')
#  {# Context creates a members object that has a property name of mymembers with a value. #}
  context = {
    'members': mymembers,   
  }
  return HttpResponse(template.render(context, request))



# Reversed within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section
# We are using members object, which has properties and property values within it,
# that can be used in numerical id order within template.html
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#                {# from .models import Member #}

#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
def for_loop_reversed(request):
# {# Add this below to create an object with all values of Member model to update Member Table #}
  mymembers = Member.objects.all().values()
#  template = loader.get_template('template.html')
  template = loader.get_template('testing/for_loop_reversed.html')
#  {# Context creates a members object that has a property name of mymembers with a value. #}
  context = {
    'members': mymembers,   
  }
  return HttpResponse(template.render(context, request))



# Empty within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #}
# We are using emptytestobject, which has an empty array with no property, 
# that can be used in template.html
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def for_emptyobject(request):
#  template = loader.get_template('template.html') Now use template below
#  template = loader.get_template('testing/for_emptyobject.html')
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
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def for_noemptyobject(request):
#  template = loader.get_template('template.html') Now use template below
#  template = loader.get_template('testing/for_noemptyobject.html')
#  {# Context creates a fruits object that has an array with property values, #}
#  {# but this object is not used in template.html . #}
# This object within context, is named fruits, but it does not have the name myobject.
# This means that it does not exist here and also there is no firstname variable in array here. 
#  context = {
#    'fruits': ['Apple', 'Banana', 'Cherry'],   
#  }
#  return HttpResponse(template.render(context, request))



# Django has some variables that are available for you inside a loop:
# We cover these forloop variables below. 

# forloop.counter within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section #}
# We are using indexes of an array here from fruits object, so it can be displayed in template.html.
# forloop.counter allows us to display array indexes in order, from 1 up top, to 5 down bottom of list on a page.
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def for_loop_counter(request):
#  template = loader.get_template('template.html') Now use template below
#  template = loader.get_template('testing/for_loop_counter.html')
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
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def for_loop_counter0(request):
#  template = loader.get_template('template.html')  Now use template below
#  template = loader.get_template('testing/for_loop_counter0.html')
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
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def for_loop_first(request):
#  template = loader.get_template('template.html')  Now use template below
#  template = loader.get_template('testing/for_loop_first.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# These array values will be displayed in a list and the first value Apple will be highlighted #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))



# forloop.last within Django for Tag (32 Django Syntax - For Loop) of Django Syntax Section 
# We are using array values here from fruits object, so it can be displayed in template.html.
# forloop.last allows us to highlight last index value from array below 
# Up top it uses {# from django.http import HttpResponse, HttpResponseRedirect #} 
#                {# from django.template import loader #}
#def testing(request): This is original testing view, but I need an individual view to keep it seperated 
# from testing page, which now has links to all examples.
# def for_loop_last(request):
#  template = loader.get_template('template.html') Now use template below
#  template = loader.get_template('testing/for_loop_last.html')
#  {# Context creates a fruits object that has an array with property values. #}
#  {# These array values will be displayed in a list and the last value Kiwi will be highlighted #}
#  context = {
#     'fruits': ['Apple','Banana','Cherry', 'Oranges', 'Kiwi'] 
#  }  
#  return HttpResponse(template.render(context, request))


# forloop.parentloop within Django for Template Tag (57 Django - Template Tag Reference) 
# of Django Reference Section 
# We are using 2 arrays here for displaying data on a page. Cars is a parent array that has a child color array.
# A counter x is being used on a cars parent array for a list and a child counter y is used to 
# nest a list of colors from that color array within this parent list. 

# Up top it uses {# from django.http import HttpResponse #} 
#                {# from django.template import loader #}
# def for_loop_parent(request):
#   template = loader.get_template('testing/for_loop_parent.html')
#   context = {
#     'cars': ['Ford', 'Volvo', 'BMW'],
#     'colors': ['Red', 'Green', 'Blue']  
#     }
#     return(template.render(context, request))


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



# Comments within Django Comment Tag of Django Comment(33 Django Syntax - Comment) in Django Syntax Section #}
#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
#    template = loader.get_template('template.html')
#    return HttpResponse(template.render()) 



# Comment Description within Django Comment Tag of Django Comment(33 Django Syntax - Comment) in Django Syntax Section #}
#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
#    template = loader.get_template('template.html')
#    return HttpResponse(template.render()) 



# Smaller Comments within Django Comment Tag of Django Comment(33 Django Syntax - Comment) in Django Syntax Section #}
#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
#    template = loader.get_template('template.html')
#    return HttpResponse(template.render())

# Use a view that has a name appropriate to this section, in this case comments
def comments_tested(request):
  template = loader.get_template('testing/comments_tested.html')
  return HttpResponse(template.render())

# Comment in Views within Django Comment Tag of Django Comment(33 Django Syntax - Comment) in Django Syntax Section #}
#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
  #template = loader.get_template('template.html')
# Change this view and give it this name comment_views, so that we can seperate it from comments view for all other 
# comments examples.   
def comment_views(request):
  template = loader.get_template('testing/comment_views.html')  
  # Views are written in Python, and Python comments are written with the # character
  # This comment in view example below, comments context, so John does not show on loclahost web page.
  #context = {
  #  'var1': 'John',
  #}
  # End of Comment in view example with context 
  return HttpResponse(template.render())   
  
  
  
# Include within Django include Tag (34 Django Include) of Django Syntax Section 
#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
  #template = loader.get_template('template.html')
  #return HttpResponse(template.render())
  
# I have decided to change this view , so that it is an example for /testing/include route.  
#def include(request):
   #template = loader.get_template('testing/include.html')
   #return HttpResponse(template.render())

# I have now decided to have this as a /testing/include_tested route, so that
# Django Include from this Django Syntax section can be seperated from include within
# Template Tag Reference of Django References. 
def include_tested(request):
  template = loader.get_template('testing/include_tested.html')  
  return HttpResponse(template.render())
  
  
# Variables in Include within Django include Tag (34 Django Include) of Django Syntax Section 
#from django.http import HttpResponse
#from django.template import loader

#def testing(request):
#  template = loader.get_template('template.html')
#  return HttpResponse(template.render()) 

# I have decided to change this view, so that it is an example for /testing/include_variables route
# or /testing/include route, I have to figure this out. I think include_variables can be in include template. 

# Comment below as I think that I may not need this 
#def include_variables(request):
  #template = loader.get_template('testing/include_variables.html')
  #return HttpResponse(template.render())


# Django References Section (57 to 59)

# Django Template Tag Reference 57 within Django References Section

# For Template page I will just use it's template below with the view
def template(request):
  template = loader.get_template('django_refs/template/template_tag_ref.html')
  return HttpResponse(template.render())

# Using Keyword Autoescape
# Autoescape Off
#def template_autoescape_off(request):

# This was used below when I included autoescape off in template route
#def template(request):
  #template = loader.get_template('template_tag_ref.html')
  #context = {
    #'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
  #}
  #return HttpResponse(template.render(context, request))

# I have decided to keep each of template tags (eg autoescape) separate from template page 
#def autoescape_off(request):
  #template = loader.get_template('django_refs/template/autoescape.html')
  #context = {
    #'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
  #}
  #return HttpResponse(template.render(context, request))

# Autoescape On
#def template(request):
  #template = loader.get_template('template_tag_ref.html')
  #context = {
    #'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
  #}
  #return HttpResponse(template.render(context, request))

#def autoescape_on(request):
  #template = loader.get_template('django_refs/template/autoescape.html')
  #context = {
    #'heading_on': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
  #}
  #return HttpResponse(template.render(context, request))

# Autoescape specifies if autoescape mode is on or off.
# It is used on a block of code with it on when it is escaped and off when not escaped. 
# Autoescap#e view can be use for both examples (on and off) on autoescape page.
def autoescape(request):
  template = loader.get_template('django_refs/template/autoescape.html')
  context = {
    'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
  }
  return HttpResponse(template.render(context, request))

# Block Template Tag Specifies a block section
def block(request):
  template = loader.get_template('django_refs/template/block.html')
  return HttpResponse(template.render())  

# Using block child template to replace block userinfo
def blockchild(request):
  template = loader.get_template('django_refs/template/blockchild.html')
  return HttpResponse(template.render())

# USe comment to specify a comment section.
def comment(request):
  template = loader.get_template('django_refs/template/comment.html')
  return HttpResponse(template.render())
  
# Use cycle to specify content to use in each cycle of a loop.
def cycle(request):  
  template = loader.get_template('django_refs/template/cycle.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))
  
# This extends view below is for extends page and does not include extends example.   
def extends(request):
  template = loader.get_template('django_refs/template/extends.html')
  return HttpResponse(template.render()) 
  
# Use extends to specify a parent template to use in a child template.  
def extends_example(request):  
  template = loader.get_template('django_refs/template/childtemplate.html')  
  return HttpResponse(template.render())
  
# Use filter to filter content before returning (displaying) it.  
def filter_tag(request):
  template = loader.get_template('django_refs/template/filter_tag.html')
  return HttpResponse(template.render())  

# Use firstof to return (display) first not empty variable.
# This firstof view below is for 1st example that has no empty variables
def firstof(request):
  template = loader.get_template('django_refs/template/firstof.html')
  context = {
    'x': 'Volvo', 'y': 'Ford', 'z': 'BMW',
  }
  return HttpResponse(template.render(context, request))

#This firstof_empty view is for 2nd example that has an 1 empty variable.
#def firstof_empty(request):
  #template = loader.get_template('django_refs/template/firstof_empty.html')
  #context = {
    #'x': '', 'y': 'Ford', 'z': 'BMW',
  #}
  #return HttpResponse(template.render(context, request))

# Use for to specify a for loop.


# Use if to specify an if statement.


# Use ifchanged in for loops. Outputs a block only if a value has changed since last iteration.


# Use include to specify included content/template. 
#comment for now include, so that I can get testing include sorted out first
# testing include in Django Syntax section is now sorted with testing/include_tested
def include(request):
  template = loader.get_template('django_refs/template/include.html')
  return HttpResponse(template.render())

# Use lorem to output random text.
def lorem(request):
  template = loader.get_template('django_refs/template/lorem.html')
  return HttpResponse(template.render())

# Use now to output (display) curent date/time.
def now(request):
  template = loader.get_template('django_refs/template/now.html')
  return HttpResponse(template.render())


# Use regroup  to sort an object by a group.
def regroup(request):
  template = loader.get_template('django_refs/template/regroup.html')
  context = {
    'cars': [
      {'brand': 'Ford', 'model': 'Mustang', 'year': '1964',},
      {'brand': 'Ford', 'model': 'Bronco', 'year': '1970',},
      {'brand': 'Ford', 'model': 'Sierra', 'year': '1981',},
      {'brand': 'Volvo', 'model': 'XC90', 'year': '2016',},
      {'brand': 'Volvo', 'model': 'P1800', 'year': '1964',},
    ]
  }
  return HttpResponse(template.render(context, request))

# Use resetcycle in cycles, as it resets a cycle that has been restarted.
def resetcycle(request):
  template = loader.get_template('django_refs/template/resetcycle.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))

# Use spaceless to remove whitespace between HTML tags. 
def spaceless(request):
  template = loader.get_template('django_refs/template/spaceless.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    }
  return HttpResponse(template.render(context, request))


# Use templatetag to output (or display) a specified template tag.
def templatetag(request):
  template = loader.get_template('django_refs/template/templatetag.html')
  return HttpResponse(template.render())

# Use verbatim to specify contents that should not be rendered by template engine.
def verbatim(request):
  template = loader.get_template('django_refs/template/verbatim.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))


# For displaying with page link
# Use with to specify a variable to use in a block
def with_template(request):
  template = loader.get_template('django_refs/template/with_template.html')
  return HttpResponse(template.render())

# Use with to create a variable to use
def with_example1(request):
  template = loader.get_template('django_refs/template/with_example1.html')
  return HttpResponse(template.render())

# Use with on a for loop method (length) on an array
def with_example2(request):
  template = loader.get_template('django_refs/template/with_example2.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))



# Django Filter Reference 58 within Django References Section

# Using Keyword Add
def filter(request):
  template = loader.get_template('django_refs/filter/filter_ref.html')
  return HttpResponse(template.render())

# Add Filter Tag specifies a value for adding.
# This first example adds a price amount within a heading.
def add(request):
  template = loader.get_template('django_refs/filter/add.html')
  context = {
    'prices': [70, 35, 52],   
  }
  return HttpResponse(template.render(context, request))

# Use Add filter with a -CHECK phrase in a heading
def add_example2(request):
  template = loader.get_template('django_refs/filter/add_example2.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

# def addcheck is not working just yet
#def addcheck(request):
  #template = loader.get_template('add.html')
  #context = {
    #'fruits': ['Apple', 'Banana', 'Cherry'],
  #}
#return HttpResponse(template.render(context, request))

def add_example3(request):
  template = loader.get_template('django_refs/filter/add_example3.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'vegetables': ['Asparagus', 'Broccoli', 'Carrot'],
  }
  return HttpResponse(template.render(context, request))


# Addslashes Filter Tag Adds a slash before any quote characters, to escape strings.
def addslashes(request):
  template = loader.get_template('django_refs/filter/addslashes.html')
  context = {
    'name': "Capt'n Jack"
  }
  return HttpResponse(template.render(context, request))  


#Capfirst filter capitalizes first letter of a value.
def capfirst(request):
  template = loader.get_template('django_refs/filter/capfirst.html')
  context = {
    'animal': 'lion',
  }
  return HttpResponse(template.render(context, request))

# Center filter places value in center of a value of specified length.
def center(request):
  template = loader.get_template('django_refs/filter/center.html')
  context = {
    'name': 'Tobias',
  }
  return HttpResponse(template.render(context, request))

def cut(request):
  template = loader.get_template('django_refs/filter/cut.html')
  context = {
    'name': 'Emil Refsnes',
  }
  return HttpResponse(template.render(context, request))

# Returns a specified value if value is False.
def default(request):
  template = loader.get_template('django_refs/filter/default.html')
  context = {
    'colors': ['Red', 'Green', 'Blue', '', 'Yellow']
  }
  return HttpResponse(template.render(context, request))

# Returns specified value if value is None. 
def default_if_none(request):
  template = loader.get_template('django_refs/filter/default_if_none.html')
  context = {
    'colors': ['Red', None, 'Blue', '', 'Yellow']
  }
  return HttpResponse(template.render(context, request))

# Sorts a dictionary by given value
def dictsort(request):
  template = loader.get_template('django_refs/filter/dictsort.html')
  context = {
    'cars': [
      {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
      {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
      {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
      {'brand': 'Ford', 'model': 'Focus', 'year': 2004},
    ]
  }
  return HttpResponse(template.render(context, request))

# Sorts a dictionary descending by year
def dictsortreversed(request):
  template = loader.get_template('django_refs/filter/dictsortreversed.html')
  context = {
    'cars': [
      {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
      {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
      {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
      {'brand': 'Ford', 'model': 'Focus', 'year': 2004},
    ]
  }
  return HttpResponse(template.render(context, request))

#Use divisibleby filter to show if a value is divisible by an argument.
#If it is divisible show true or yes, otherwise show false.
def divisibleby(request):
  template = loader.get_template('django_refs/filter/divisibleby.html')
  context = {
    'totalsum': 40,
  }
  return HttpResponse(template.render(context, request))

# Use escape filter to display text containing HTML, with and without escape
def escape(request):
  template = loader.get_template('django_refs/filter/escape.html')
  context = {
    'heading': 'Hello &lt;i>my&lt;/i> World!',
  }
  return HttpResponse(template.render(context, request))

# Use escapejs filter to escape text that is used in a JavaScript strings
def escapejs(request):
  template = loader.get_template('django_refs/filter/escapejs.html')
  context = {
    'var1': 'John\nDoe',  
  }
  return HttpResponse(template.render(context, request))

#Displays a number into a file size format
def filesizeformat(request):
  template = loader.get_template('django_refs/filter/filesizeformat.html')
  context = {
    'size': 26214400    
  }
  return HttpResponse(template.render(context, request))

#Use First to display first item of an object (for Strings, the first character is returned).
def first(request):
  template = loader.get_template('django_refs/filter/first.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))

# Also use first filter on strings for displaying first character
def first_example2(request):
  template = loader.get_template('django_refs/filter/first_example2.html')
  context = {
    'firstname': 'Emil',
    'lastname': 'Refsnes',
  }
  return HttpResponse(template.render(context, request))

# Use floatformat to round floating numbers to a specified number of decimal places. 
# Round a number to only two decimal places
def floatformat(request):
  template = loader.get_template('django_refs/filter/floatformat.html')
  context = {
    'mynumber': 7.122489,
  }
  return HttpResponse(template.render(context, request))

# Use Floatformat with Positive Decimal Number
def floatformat_example2(request):
  template = loader.get_template('django_refs/filter/floatformat_example2.html')
  return HttpResponse(template.render())

# Use Floatformat with Negative Decimal Number
def floatformat_example3(request):
  template = loader.get_template('django_refs/filter/floatformat_example3.html')
  return HttpResponse(template.render())

# Use Floatformat with g Argument
def floatformat_example4(request):
  template = loader.get_template('django_refs/filter/floatformat_example4.html')
  context = {
    'mynumber': 981358286,
  }
  return HttpResponse(template.render(context, request))

# Use get_digit to display a specific digit of a number.
def get_digit(request):
  template = loader.get_template('django_refs/filter/get_digit.html')
  context = {
    'mynumber': 75641,
  } 
  return HttpResponse(template.render(context, request))

# Use join filter to take all items in an iterable and joins them into one string.
def join(request):
  template = loader.get_template('django_refs/filter/join.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))

# Use json_object to convert an object into a JSON object surrounded by <script></script> tags.
def json_script(request):
  template = loader.get_template('django_refs/filter/json_script.html')
  context = {
    'cars': [
      {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
    ]
  }
  return HttpResponse(template.render(context, request))

# Use last filter to display last item of an object (for strings last character is displayed).
def last(request):
  template = loader.get_template('django_refs/filter/last.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))

# Also use last filter on strings for displaying last character
def last_example2(request):
  template = loader.get_template('django_refs/filter/last_example2.html')
  context = {
    'firstname': 'Emil',
    'lastname': 'Refsnes',
  }
  return HttpResponse(template.render(context, request))

# Use length filter for displaying number of items in an object
def length(request):
  template = loader.get_template('django_refs/filter/length.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
  }
  return HttpResponse(template.render(context, request))

# Also use length filter on strings for displaying number of characters
def length_example2(request):
  template=loader.get_template('django_refs/filter/length_example2.html')
  context = {
    'firstname': 'Emil',
    'lastname': 'Refsnes',
  }
  return HttpResponse(template.render(context, request))

# Use length_is filter like a boolean to determine if an object has a specified length.
def length_is(request):
  template = loader.get_template('django_refs/filter/length_is.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

# Use length_is filter with a Django If Statement to display something, like a heading.
def length_is_example2(request):
  template = loader.get_template('django_refs/filter/length_is_example2.html')
  context = {
    'firstname': 'Linus',
    'lastname': 'Refsnes',
  }
  return HttpResponse(template.render(context, request))

# Use linebreaks filter to create linebreaks, which would normally be done with < br > tag.
# linebreaks filter can also be used to create a paragraph with double line breaks. 
def linebreaks(request):
  template = loader.get_template('django_refs/filter/linebreaks.html')
  context = {
    'mytext': 'Hello\nmy name is Leo.\n\nI am a student.',
  }
  return HttpResponse(template.render(context, request))

# Use linebreaksbr to display text with <br> instead of line breaks.
def linebreaksbr(request):
  template = loader.get_template('django_refs/filter/linebreaksbr.html')
  context = {
    'mytext': 'Hello\nmy name is Leo.\n\nI am a student.',   
  }
  return HttpResponse(template.render(context, request)) 

# Use linenumbers filter to ad a line number before each line of a text.
def linenumbers(request):
  template = loader.get_template('django_refs/filter/linenumbers.html')
  context = {
    'mytext': 'Hello\nmy name is Leo. \n\nI am a student.',
  }
  return HttpResponse(template.render(context, request))

# Use lower filter to display a value in all lower case letters. 
def ljust(request):
  template = loader.get_template('django_refs/filter/ljust.html')
  context = {
    'firstname': 'Tobias',
  }
  return HttpResponse(template.render(context, request))

# Use lower filter to display a value in all lower case letters. 
def lower(request):
  template = loader.get_template('django_refs/filter/lower.html')
  context = {
    'firstname': 'Tobias',
  }
  return HttpResponse(template.render(context, request))

# Use make_list filter to convert a value into a list object.
def make_list(request):
  template = loader.get_template('django_refs/filter/make_list.html')
  context = {
    'name': 'Emil Refsnes',
  }
  return HttpResponse(template.render(context, request))

# Use phone2numeric filter to convert phone numbers with letters into numeric phone numbers.
def phone2numeric(request):
  template = loader.get_template('django_refs/filter/phone2numeric.html')
  context = {
    'phone': '555-autmobile'
  }
  return HttpResponse(template.render(context, request))

# Use pluralize to add a suffix to end of a word.
def pluralize(request):
  template = loader.get_template('django_refs/filter/pluralize.html')
  context = {
    'arr': [0, 1 ,2]
  }
  return HttpResponse(template.render(context, request))

# Use random filter to display a random item of an object.
def random(request):
  template = loader.get_template('django_refs/filter/random.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Orange'],
  }
  return HttpResponse(template.render(context, request))
  
# Use rjust filter to right align a value according to a specified width.  
def rjust(request):
  template = loader.get_template('django_refs/filter/rjust.html')
  context = {
    'name': 'Tobias',
  }
  return HttpResponse(template.render(context, request))

#Use slice filter to display a specified slice of a text or object.
def slice(request):
  template = loader.get_template('django_refs/filter/slice.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Kiwi', 'Orange'],
  }
  return HttpResponse(template.render(context, request))

# Use slugify filter to Converts text into one long alphanumeric-lower-case word.
# Can be very useful for web urls and text.  
def slugify(request):
  template = loader.get_template('django_refs/filter/slugify.html')
  context = {
    'text': 'Hi, my name is Linus',
  }
  return HttpResponse(template.render(context, request))

# Use slugify on non alphanumeric characters
def slugify_example2(request):
  template = loader.get_template('django_refs/filter/slugify_example2.html')
  return HttpResponse(template.render())


# Use striptags filter to remove any HTML tags from a value
def striptags(request):
  template = loader.get_template('django_refs/filter/striptags.html')
  context = {
    'mytext': '&lt;h1>Welcome to &lt;b>MY&lt;/b> World!&lt;/h1>',
  }
  return HttpResponse(template.render(context, request))

# Use time filter to display a time in a specified format
import datetime

def time(request):
  template = loader.get_template('django_refs/filter/time.html')
  context = {
    'mydate': datetime.datetime.now(),   
  }
  return HttpResponse(template.render(context, request))

# Use timesince filter to display difference between two date times. 
import datetime

def timesince(request):
  template= loader.get_template('django_refs/filter/timesince.html')
  context = {
    'mybirthdate': datetime.datetime(1975, 4, 21),
    'mydate': datetime.datetime(2024, 1, 15)
  }
  return HttpResponse(template.render(context, request))

# Using timesince for difference between two date times and leaving out date in argument. 
def timesince_example2(request):
  template = loader.get_template('django_refs/filter/timesince_example2.html')
  context = {
    'mybirthdate': datetime.datetime(1975, 4, 21),
  }
  return HttpResponse(template.render(context, request))

# Use timesince for difference between two times, in hours and minutes
def timesince_example3(request):
  template = loader.get_template('django_refs/filter/timesince_example3.html')
  context = {
    'date1': datetime.datetime(2022, 6, 8, 9, 30),
    'date2': datetime.datetime(2022, 6, 8, 13, 45),
  }
  return HttpResponse(template.render(context, request))

# Use timeuntil filter to display difference between 2 date times from current date now.
import datetime

def timeuntil(request):
  template = loader.get_template('django_refs/filter/timeuntil.html')
  context = {
    'marslanding': datetime.datetime(2050, 5, 17)
  }
  return HttpResponse(template.render(context, request))

# Use timeuntil and include a a default time to start the time from.   
#def timeuntil_example2(request):
  #template = loader.get_template('django_refs/filter/timeuntil_example2.html')
  #context = {
    #'marslanding': datetime.datetime(2050, 5, 17),
    #'moonlanding': datetime.datetime(1969, 7, 20),
  #}
  #return HttpResponse(template.render(context, request))

# Use timeuntil for time difference in hours and minutes 
#def timeuntil_example3(request):
  #template = loader.get_template('django_refs/filter/timeuntil_example3.html')
  #context = {
    #'date1': datetime.datetime(2022, 6, 8, 17, 39),
    #'date2': datetime.datetime(2022, 6, 8, 8, 13),
  #}
  #return HttpResponse(template.render(context, request))

# Use title filter to Upper case first character of each word in a text, 
# all other characters are converted to lower case.
def title(request): 
  template= loader.get_template('django_refs/filter/title.html')
  context = {
    'mytext': 'Hello my friend, do you like DJANGO',
  }
  return HttpResponse(template.render(context, request))


# Use truncatechars to shorten a string into a specified number of characters.
def truncatechars(request):
  template = loader.get_template('django_refs/filter/truncatechars.html')
  context = {
    'mytext': 'Hello my friend, do you like DJANGO',   
  }
  return HttpResponse(template.render(context, request))  

# Use truncatechars_html to shorten a string into a specified number of characters and it does not consider length of any HTML tags.
def truncatechars_html(request):
  template = loader.get_template('django_refs/filter/truncatechars_html.html')
  context = {
    'mytext': '&lt;h1>Hello my friend, do you like DJANGO?&lt;/h1>',
  }
  return HttpResponse(template.render(context, request))
  
# Use truncatewords to shorten a string into specified number of words. 
def truncatewords(request):
  template = loader.get_template('django_refs/filter/truncatewords.html')
  context = {
    'mytext': 'Hello my friend, do you like DJANGO',
  }
  return HttpResponse(template.render(context, request))

# Use truncatewords_html to shorten a string into a specified number of words and it does not consider any HTML tags.
def truncatewords_html(request):
  template = loader.get_template('django_refs/filter/truncatewords_html.html')
  context = {
    'mytext': '&lt;h1>Hello my friend, do you like DJANGO?&lt;/h1>',
  }
  return HttpResponse(template.render(context, request))


# Use unordered_list to convert django or python list from an object array into an HTML list
def unordered_list(request):
  template = loader.get_template('django_refs/filter/unordered_list.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Kiwi', 'Orange'],
  }
  return HttpResponse(template.render(context, request))

# Use unordered_list for nested list as well to convert into HTML list
def unordered_list_nested(request):
  template = loader.get_template('django_refs/filter/unordered_list_nested.html')
  context = {
    'food': ['Seafood', 
             ['Fish', 'Lobster'], 
                'Vegetables', 
                ['Carrots', 'Broccoli']],
  }
  return HttpResponse(template.render(context, request))

# Use upper filter to display text in upper case letters. 
def upper(request):
  template = loader.get_template('django_refs/filter/upper.html')
  context = {
    'firstname': 'Tobias'
  }
  return HttpResponse(template.render(context, request))


# Django Field Lookups Reference 59 within Django References Section

def field(request):
  template = loader.get_template('django_refs/field/field_lookups_ref.html')
  return HttpResponse(template.render())

# Using Keyword Contains
#def field(request):
  #mydata = Member.objects.filter(firstname__contains='bias').values()
  #template = loader.get_template('field_lookups_ref.html')
  #context = {
    #'mymembers': mydata,
  #}
  
  #return HttpResponse(template.render(context, request))

# Contains Field Lookup is used to get records that contain a specified value and it is case sensitive. 
def contains(request):
   mydata = Member.objects.filter(firstname__contains='bias').values()
   template = loader.get_template('django_refs/field/contains.html')
   context = {
     'mymembers': mydata,
   }
   return HttpResponse(template.render(context, request))

# Icontains Field Lookup is used to get records that contains a specified value and it is case insensitive.
def icontains(request):
  mydata = Member.objects.filter(lastname__icontains='ref').values()
  template= loader.get_template('django_refs/field/icontains.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out icontains.html to see how mymembers object was used in HTML Code.


# Using Keyword Endswith

#def field(request):
  #mydata = Member.objects.filter(firstname__endswith='s').values()
  #template = loader.get_template('field_lookups_ref.html')
  #context = {
    #'mymembers': mydata,
  #}
  #return HttpResponse(template.render(context, request))
          
# Check out template.html to see how the mymembers object
# was used in the HTML code.     

# endswith lookup is used to get records that end with a specified value.
def endswith(request):
  mydata = Member.objects.filter(firstname__endswith='s').values()
  template = loader.get_template('django_refs/field/endswith.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out templates/django_refs/field/endswith.html to see how mymembers object was used in HTML code. 

def iendswith(request):
  mydata = Member.objects.filter(firstname__endswith='s').values()
  template = loader.get_template('django_refs/field/iendswith.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out templates/django_refs/field/iendswith.html to see how mymembers object was used in HTML code.

# exact lookup is used to get records with a specified value.
def exact(request):
  mydata = Member.objects.filter(firstname__exact='Emil').values()
  template = loader.get_template('django_refs/field/exact.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
# Check out templates/django_refs/field/exact.html to see how mymembers object was used in HTML code. 

# iexact lookup is used to get records with a specified value.
def iexact(request):
  mydata = Member.objects.filter(firstname__iexact='Emil').values()
  template = loader.get_template('django_refs/field/iexact.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
# Check out templates/django_refs/field/iexact.html to see how mymembers object was used in HTML code.  

# in lookup is used to get records where a value is one of values in an iterable (list, tuple, string, queryset).
#def in(request):
  #mydata = Member.objects.filter(firstname__in)=['Tobias', 'Linus', 'John']
  #template = loader.get_template('django_refs/field/in.html')
  #context = {
    #'mymembers': mydata,
  #}
  #return HttpResponse(template.render(context, request)) 

# Check out templates/django_refs/field/in.html to see how mymembers object was used in HTML code.

# gt lookup is used to get records that are larger than a specified value.
def gt(request):
  mydata = Member.objects.filter(id__gt=3).values()
  template = loader.get_template('django_refs/field/gt.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request)) 

# Check out templates/django_refs/field/gt.html to see how mymembers object was used in HTML code.  

# gte lookup is used to get records that are larger than, or equal to, a specified value.
def gte(request):
  mydata = Member.objects.filter(id__gte=3).values()
  template = loader.get_template('django_refs/field/gte.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out templates/django_refs/field/gte.html to see how mymembers object was used in HTML code.  

# lt lookup is used to get records that are larger than, or equal to, a specified value.
def lt(request):
  mydata = Member.objects.filter(id__lt=3).values()
  template = loader.get_template('django_refs/field/lt.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out templates/django_refs/field/lt.html to see how mymembers object was used in HTML code.

# lt lookup is used to get records that are larger than, or equal to, a specified value.
def lte(request):
  mydata = Member.objects.filter(id__lte=3).values()
  template = loader.get_template('django_refs/field/lte.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out templates/django_refs/field/lte.html to see how mymembers object was used in HTML code.

def startswith(request):
  mydata = Member.objects.filter(firstname__startswith='S').values()
  template = loader.get_template('django_refs/field/startswith.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out templates/django_refs/field/startswith.html to see how mymembers object was used in HTML code.

def istartswith(request):
  mydata = Member.objects.filter(firstname__istartswith='s').values()
  template = loader.get_template('django_refs/field/istartswith.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

# Check out templates/django_refs/field/istartswith.html to see how mymembers object was used in HTML code.
