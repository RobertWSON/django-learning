from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    # Django Update Model
    # Add 2 Fields in Model
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
    # Change String Representation Function
    # Use a defined string function for the Member Model
    # self part relates to an object, see w3schools.com/python/ref_func_str.asp 
    # found from __str__ what does return f"{}" do 
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    # I want to find out what f does with return
    # From __str__ what does return f"{}" do, I found this 
    # datacamp.com/tutorial/f-string-formatting-in-python
    # and variables can be displayed using curly {} braces 
    