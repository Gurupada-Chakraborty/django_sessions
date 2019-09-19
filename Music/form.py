#creating user form model
from django.contrib.auth.models import User
from django import forms

#class based model form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: #info about class
            model = User
            fields = ['username', 'password', 'email']

