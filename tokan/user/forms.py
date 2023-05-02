from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 100)
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
