from django.forms import forms,extras
from django import forms
#To add a User into the database


class Add(forms.Form):
    Username = forms.CharField(label='Your name', max_length=100,initial=" ")
    Password=forms.CharField(widget=forms.PasswordInput,label="Password",initial=" ")
    Email = forms.EmailField(label="Email Id:", initial="",)

    DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
           '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
           '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003')

    DOB = forms.DateField(label="Date of Birth",widget=extras.SelectDateWidget(years=DOY))
    Description=forms.CharField(label="Describe Yourself",widget=forms.Textarea)
    OPTIONS=(("Java","Java"),("C++","C++"),("C","C"),("Python","Python"),("JavaScript","JavaScript"),("Ruby","Ruby"))
    Languages=forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS,
    )
