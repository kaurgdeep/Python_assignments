from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'semirestful_app/index.html',context)

def new(request):
    return render(request,'semirestful_app/new.html') 

def createUser(request):
    #lots of code here
    #to create a new user
    return redirect('/')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'semirestful_app/edit.html', context)    

