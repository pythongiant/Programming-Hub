from django.forms import forms

#To add a User into the database

from django import forms

class Add(forms.Form):
    Username = forms.CharField(label='Your name', max_length=100,initial=" ")
    Password=forms.CharField(widget=forms.PasswordInput,label="password",initial=" ")
    Email = forms.EmailField(label="Email Id:", initial="",)
