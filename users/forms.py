from attr import field
from django import forms
from django.contrib.auth.models import User #inbuit model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    # we wamt to add additional field 
    email = forms.EmailField()
    # parentage = forms.CharField()
    
    class Meta: # class which provide information about the class itself (registerform)
        model = User  # this  form  belong to user model
        fields = ['username' , 'email']
        
