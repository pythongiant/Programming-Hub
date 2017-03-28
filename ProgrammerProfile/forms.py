from django.forms import forms,extras
from django import forms
#To add a User into the database


class Add(forms.Form):
    Username = forms.CharField(label='Your name', max_length=100,initial=" ")
    Password=forms.CharField(widget=forms.PasswordInput,label="Password",initial=" ")
    Email = forms.EmailField(label="Email Id:", initial="",)
    age=forms.IntegerField(label="Your age")
    Description=forms.CharField(label="Describe Yourself",widget=forms.Textarea)
    OPTIONS=(("Java","Java"),("C++","C++"),("C","C"),("Python","Python"),("JavaScript","JavaScript"),("Ruby","Ruby"))
    Languages=forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS,
    )
