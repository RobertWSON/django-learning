

# comment this actual code     
from django.contrib import admin 

# Use models to make Member model visible in admin page

# comment this actual code    
from .models import Member


# Register your models here.

# Below is an example of a ModelAdmin class, which is a representation of a model in an admin interface.
# see docs.djangoproject.com/en/4.2/ref/contrib/admin 
# We have also set string values for list_display property 
# see juhanajauhiainen.com/psots/customize-django-admin-with-list-display-property
# all found from django set list display google search


# comment this actual code     
class MemberAdmin(admin.ModelAdmin):    # Note: ModelAdmin is an object for members in admin page 

    
   # comment this actual code
   list_display = ("firstname", "lastname", "joined_date",)
   # This is a tuple
   # Specify a list_display tuple to display as a table with values instead of a plain list
   
# comment this actual code      
admin.site.register(Member, MemberAdmin)

  
# Here we are pushing interface class (MemberAdmin) with original model class (Member) 
# to admin.site.register function. Refer to Introduction to ModelAdmin section on this website 
# medium.com/nerd-for-tech/from-zero-to-hero-django-admin-modeladmin-class-part2-2c8665d6cd5 .
# Member model name is initially registered in Django Admin, so it appears in Django Admin Interface,
# for example showing as Member object (1) initially.
# Now though we are using MemberAdmin as a class for displaying each member with a person's name in Django Admin,
# so string representation has changed and Emil is now showing instead of Member object (1).    