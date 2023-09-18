
# comment this actual code   
from django.db import models
# Here we are importing models from a django database library 


# Create your models here.

# Create Table (Model), within Django Models (9 Django URLs) of Django Tutorial Section
# comment this actual code   
class Member(models.Model):
# Here a class is created and we are using a models library for the Model Table (a database)     
    
    
    # comment this actual code   
    firstname = models.CharField(max_length=255)
    # comment this actual code   
    lastname = models.CharField(max_length=255)
    
    
    # We are creating variables (firstname and lastname) and using a models library to get a Field from Model 
    # Table. In this case Charfield is a character field that can take a string with up to 255 characters
    # Charfield is a string field for small to large sized strings. 
    # It uses a Max_length required argument as an attribute, inside brackets 
    # (much like parameter does with a function).
    # see geeksforgeeks.org/charfield-django-models/ found from Django charfield google search   


# Add Fields in the Model, within Django Update Model (15 Django Update model) of Django Tutorial Section   
    # Add 2 Fields in Model before migration process
    
    
    # comment this actual code     
    phone = models.IntegerField(null=True)
    # comment this actual code     
    joined_date = models.DateField(null=True)
    
    
    # After these 2 fields are added, we do a migration process that tells Django to update changes in database
    # for these new fields.
    # Default is set to false, I have to change this 
    # null=true is added within () above, when selecting option 2, during migration process
    # null=true allows for two possible values for “no data”: NULL and an empty string     
    # 
     
     
# Change the String Representation Function within Django Admin - Set Fields to Display  
# (25 Django Admin - Set List Display) of Django Admin Section
    # Use a defined string function for the Member Model
    # self part relates to an object, see w3schools.com/python/ref_func_str.asp 
    # found from __str__ what does return f"{}" do 
    
    
    # comment this actual code     
    def __str__(self):
        # comment this actual code   
        return f"{self.firstname} {self.lastname}"
    
    
    # I want to find out what f does with return
    # From __str__ what does return f"{}" do, I found this 
    # datacamp.com/tutorial/f-string-formatting-in-python
    # and variables can be displayed using curly {} braces 
    