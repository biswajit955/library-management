from django import forms
from django.contrib.auth.models import User
from . import models
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = [ 'first_name','last_name','email', 'password1', 'password2']





class StudentUserForm(forms.ModelForm):
    class Meta:
        model=models.MyUser
        fields='__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category']

    
