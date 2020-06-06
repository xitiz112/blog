from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupViewForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('email','username','password1','password2')

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('email','username')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["image"]
