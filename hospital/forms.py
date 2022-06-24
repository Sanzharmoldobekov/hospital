from django import forms
from .models import Patient
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


