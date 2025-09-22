from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, help_text="Enter your name")
    email = forms.EmailField(max_length=254, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')
