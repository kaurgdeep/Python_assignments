from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request,'friend_app/index.html')

def processreg(request):
    result = User.objects.validate_registration(request.POST)
    if result['status']:    #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/friends')
    else:
        for error in result['errors']:
            messages.error(request,error)   
    return redirect('/')


def processlog(request):
    result = User.objects.validate_login(request.POST)
    if result['status']: #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/friends')
    else:
        for error in result['errors']:
            messages.error(request,error)    
    return redirect('/')
def logout(request):
    request.session.clear() 
    return redirect('/')
def home(request):
    return redirect('/friends')

def success(request):
    return render(request, 'friend_app/friends.html')


