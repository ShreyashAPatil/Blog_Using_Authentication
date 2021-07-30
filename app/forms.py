from django import forms
from . models import blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class blog_form(forms.ModelForm):
    class Meta:
        model=blog
        fields="__all__"

title=forms.CharField(widget=forms.TextInput({"Placeholder":"Enter your title"}))
content=forms.CharField(widget=forms.TextInput({"Placeholder":"Write your content"}))
image=forms.ImageField()
date=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))



class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","Email_address","password1","password2")

    username = forms.CharField()
    Email_address = forms.EmailField(label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')