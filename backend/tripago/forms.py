from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username', 
                  'email',
                  'password1', 
                  'password2'
                  ]
        
# Authenticate a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))