from django.shortcuts import render
from .forms import  Add

def index(request):
    return render(request, "ProgrammerProfile/index.html", {})

def signup(request):
    form=Add()
    context={
        "form":form,
    }
    return render(request, "ProgrammerProfile/form.html",context)