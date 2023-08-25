
# Here we are importing models from a django database library 
from django.db import models


# Create your models here.

# Create Table (Model), within Django Models (9 Django URLs) of Django Tutorial Section
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

# Add Fields in the Model, within Django Update Model (15 Django Update model) of Django Tutorial Section   
    # Add 2 Fields in Model before migration process
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    # After these 2 fields are added, we do a migration process that tells Django to update changes in database
    # for these new fields.
    # Default is set to false, I have to change this 
    # null=true is added within () when selecting option 2, during migration process
    # null=true allows for two possible values for “no data”: NULL and an empty string     
    # 
     
     
# Change the String Representation Function within Django Admin - Set Fields to Display  
# (25 Django Admin - Set List Display) of Django Admin Section
    # Use a defined string function for the Member Model
    # self part relates to an object, see w3schools.com/python/ref_func_str.asp 
    # found from __str__ what does return f"{}" do 
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    # I want to find out what f does with return
    # From __str__ what does return f"{}" do, I found this 
    # datacamp.com/tutorial/f-string-formatting-in-python
    # and variables can be displayed using curly {} braces 
    