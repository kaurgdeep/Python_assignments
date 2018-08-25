from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request,'belt_app/index.html')

def processreg(request):
    result = User.objects.validate_registration(request.POST)
    if result['status']:    #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error)   
    return redirect('/')


def processlog(request):
    result = User.objects.validate_login(request.POST)
    if result['status']: #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error)    
    return redirect('/')
    
def create_item(request):
    result = Item.objects.validate_item(request.POST)
    if result['status']:
        request.session['item_id'] = result['item_id']
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error)
    print('helllooooo')
        
    return redirect('/create')



def logout(request):
    request.session.clear() 
    return redirect('/')
def home(request):
    return redirect('/success')

def success(request):
    return render(request, 'belt_app/success.html')

def create(request):
    return render(request, 'belt_app/create.html')


