from django import forms
from django.contrib.auth.models import User      #from admin
from django.contrib.auth.forms import UserCreationForm        #forms to make the registration

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()                           #added fields to be displayed or to must be filed up 
    

    class Meta:                 
        model = User
        fields = ['username','email','password1','password2']         #fields to be displayed or to must be filed up 