from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # first_name = forms.CharField(max_length=100, help_text='Last Name')
    # last_name = forms.CharField(max_length=100, help_text='Last Name')
    age = forms.IntegerField()
    
class Meta:
    model = User
    Field = ['username', 'email','age', 'password1', 'password2']    