from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# register a user
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
        
# authenticate a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# create an itinerary
class ItineraryGenerationForm(forms.Form):
    city = forms.CharField(widget=TextInput())
    country = forms.CharField(widget=TextInput())