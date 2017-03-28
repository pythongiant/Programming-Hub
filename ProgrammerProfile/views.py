from django.shortcuts import render,redirect
from django.contrib.auth.models import User #Import the User module
from django.contrib.auth import authenticate,login,logout#import some more stuff
from .forms import Add
from .models import *

def index(request):
    return render(request, "ProgrammerProfile/index.html", {})

def signup(request):
    form=Add()
    context={"form":form}

    return render(request, "ProgrammerProfile/form.html",context)


def SignUpAction(request):
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            email = form.cleaned_data['Email']
            language=form.cleaned_data['Languages']
            description=form.cleaned_data['Description']

            user = User.objects.create_user(username, email, password)

    return redirect("/photos/login")
