from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'first_app/index.html')

def processreg(request):
    result = User.objects.validate_registration(request.POST)
    if result['status']:    #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/index2')
    else:
        for error in result['errors']:
            messages.error(request,error)   
    return redirect('/')


def processlog(request):
    result = User.objects.validate_login(request.POST)
    if result['status']: #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/index2')
    else:
        for error in result['errors']:
            messages.error(request,error)    
    return redirect('/')

def index2(request):
    return render(request, 'first_app/index2.html')

def logout(request):
    request.session.clear() 
    return redirect('/')
   