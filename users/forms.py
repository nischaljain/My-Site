from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default is required = True

    class Meta:
        #inside class meta, we provide the model the form is supposed to interact with
        model = User
        fields = ['username','email','password1','password2']