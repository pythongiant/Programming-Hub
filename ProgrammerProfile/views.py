from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User #Import the User module
from django.contrib.auth import authenticate,login,logout#import some more stuff
from .forms import *
from .models import *

def index(request):
    return render(request, "ProgrammerProfile/index.html", {})

def signup(request):
    form=Add()
    context={"form":form}

    return render(request, "ProgrammerProfile/form.html",context)


def SignUpAction(request):
    if request.method == 'POST':
        form = Add(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            age=form.cleaned_data['age']
            email = form.cleaned_data['Email']
            language = form.cleaned_data['Languages']
            description = form.cleaned_data['Description']
            Profile_pic=form.cleaned_data["Profile_Picture"]
            user = User.objects.create_user(username, email, password)
            Person.objects.create(Name=username,age=age,Description=description,ProfilePic=Profile_pic)
            for i in language:
                Language.objects.create(user=user,Language=i)
            user=authenticate(username=username,password=password)
            login(request,user)
    return redirect("/home")


def loginuser(request):
    form = Authenticate()
    return render(request, 'ProgrammerProfile/login.html', {'Login': form})


def log(request):

    if request.method == 'POST':
        form = Authenticate(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/home')
            else:
                return render(request,"ProgrammerProfile/invalid.html",{})


def outlog(request):
   logout(request)
   return redirect("/")

def home(request):
    a = Person.objects.all()
    context={
        "everybody":a
    }
    return render(request, "ProgrammerProfile/home.html", context)


def user_detail(request,user_id):
    person = get_object_or_404(Person, pk=user_id)
    language = Language.objects.filter(user=person.Name)
    context={
        "person" : person,
        "language":language
    }
    return render(request,"ProgrammerProfile/detail.html",context)