from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from .models import Profile



class RegisterForm(UserCreationForm):
    GENDER_CHOICES = (
        ('M', 'Male',),
        ('F', 'Female',),
        ('U', 'Others',),
    )
    gender=forms.ChoiceField(choices=GENDER_CHOICES,)
    contact_no=forms.IntegerField()
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    checkbx=forms.BooleanField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'example@yourserver.com'})
        self.fields['contact_no'].widget.attrs.update({'placeholder': '(+91) 97********'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City'})
        self.fields['country'].widget.attrs.update({'placeholder': 'Country'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'New Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "gender",  "contact_no", "city", "country",  "password1", "password2","checkbx",]




class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username Or Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ["username",  "password",]


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=["gender",  "contact_no", "city", "country","profile_image"]
