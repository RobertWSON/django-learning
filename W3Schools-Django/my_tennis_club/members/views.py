from django.shortcuts import render
from django.http import HttpResponse
# Use loader to Modify web page view
from django.template import loader
# import Member Model, so we can use it display info from its Table  
from .models import Member


# Create your views here.

# View that makes member model data in members folder, available from a template
def members(request):
    # Add this to create an object with all values of Member model to update Member Table
    mymembers = Member.objects.all().values()   
    # HTML Template to be used with loader
    # template = loader.get_template('myfirst.html')
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
    return HttpResponse(template.render(context, request))

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

# View for dealing with incoming requests to root / of the project (main home landing page)
def main(request):
    # HTML main Template to be used with loader (Load main html template)
    template = loader.get_template('main.html')
    # Output HTML that is rendered by template. W3Schools does not include request with render for some reason.
    return HttpResponse(template.render())

# View for dealing with testing different aspects of Django, 
# as it can be a good idea to have somewhere to test code without destroying main project.
# The View can deal with incoming rquests from a /testing/ url, to see how the testing works.  
def testing(request):
    # HTML Template to be used with loader (load Template html file)
    template = loader.get_template('template.html')
    # Creates an object containing fruits as an array
    #context = {       # fruits is the object name  
        # 'fruits': ['Apple', 'Banana', 'Cherry'],  # fruits object is an Array that has a variety of fruits   
        #'firstname': 'Linus' , # HTMLTemplate Variable is given a name here
    #}
    
    # Sends object to template and output HTML rendered by template. 
    #return HttpResponse(template.render(context, request))

    #Use return Below for Creating Variables in Template within Django Variable of Django Syntax Section 
    return HttpResponse(template.render())

    # Data from a Model within Django Variable of Django Syntax Section    
    #def testing(request):
    #    mymembers = Member.objects.all().values()
    #    template = loader.get_template('template.html')
    #    context = {
    #        'mymembers': mymembers,
    #    }
    #    return HttpResponse(template.render(context, request))