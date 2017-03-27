from django.forms import forms

#To add a User into the database

class Add(forms.Form):
    Username=forms.CharField(label="Username:",initial=" ")
    Password=forms.CharField(widget = forms.PasswordInput(),initial="")
    Email=forms.EmailField(label="Email Id:",initial="")
