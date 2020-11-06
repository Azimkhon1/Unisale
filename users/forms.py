from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    snapchat = forms.CharField(max_length=50, required=False, label='Snapchat (Optional)')

    class Meta:
        model = User
        fields = ['username', 'snapchat', 'email', 'password1', 'password2']

