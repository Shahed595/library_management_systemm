from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . managers import User

class UserREgistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UserLogoutForm(forms.Form):
    pass      

               
    