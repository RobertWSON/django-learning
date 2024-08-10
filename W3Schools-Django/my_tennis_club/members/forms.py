
# import module to use for making our form
from django import forms

# Just like with models, use our forms module here with a class
class MemberSearchForm(forms.Form):
    member_id = forms.IntegerField(label='Member ID', required=True)
    # This is for getting an id, which is an integer from a member in our model.
    # I think required-Trues means that it is needed for form to work. 
     
    