from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User #Import the User module
from django.contrib.auth import authenticate,login,logout#import some more stuff
from .forms import *
from .models import *
#admin pass username admin password pass1234
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
            description = form.cleaned_data['Description']
            Profile_pic=form.cleaned_data["Profile_Picture"]
            user = User.objects.create_user(username, email, password)
            Person.objects.create(Name=username,age=age,Description=description,ProfilePic=Profile_pic)
            
            user=authenticate(username=username,password=password)
            login(request,user)
    return redirect("/home")


def loginuser(request):
    form = Authenticate()
    return render(request, 'ProgrammerProfile/login.html', {'Login': form})
def formPost(request):
    
    if request.method == 'POST':
        form = posts(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['Review']
            Posts.objects.create(Name=title,post=description,author=request.user.username)
    return redirect("/home")            


def post(request):
    form = posts()
    return render(request, 'ProgrammerProfile/post.html', {'form': form})

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
    article = Posts.objects.filter(author=person.Name)
    if len(article) == 0 :
        article=[""]
        article[0]="None"
    context={
        "person" : person,
        "article" : article

    }
    return render(request,"ProgrammerProfile/detail.html",context)

def article_detail(request,article_id):
    article = get_object_or_404(Posts, pk=article_id)
    
    context={
        "article" : article

    }
    return render(request,"ProgrammerProfile/article.html",context)    