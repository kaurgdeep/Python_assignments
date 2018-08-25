from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request,'main_app/index.html')

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
def logout(request):
    request.session.flush() 
    return redirect('/')
def home(request):
    return redirect('/success')

def success(request):
    context = {
        "me": User.objects.get(id=request.session['user_id']),
        "all_users": User.objects.all(),
        "all_items": Item.objects.all(),
        # "my_items": User.objects.get(id=request.session['user_id']).added_items.all(),
        "not_my_items": Item.objects.exclude(people_wish_item=request.session['user_id']),
        "my_items": Item.objects.filter(people_wish_item=request.session['user_id'])
    }
    return render(request,'main_app/success.html',context)

def create(request):
    return render(request, 'main_app/create.html')

def create_item(request):
    result = Item.objects.validate_create_item(request.POST)
    if result['status']:    #that means if its true
        post_item = request.POST['item']
        #post_created_at = request.POST['created_at']
        post_added_by = User.objects.get(id=request.session['user_id'])

        item = Item.objects.create(
            item = post_item,
            added_by = post_added_by 
            )

        item.people_wish_item.add(post_added_by)
        item.save()
        
        print(item.item)
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error) 
    return redirect('/create')

    

def wish_item(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {

        "current_item" : item,
        "other_users" : item.people_wish_item.exclude(id=item.added_by.id) 

    }
    return render(request,'main_app/wishitem.html', context)

def addlist(request, item_id):
    Item.objects.addlist(item_id, request.session['user_id'])
    return redirect('/success')

def remove_list(request, item_id):
    Item.objects.remove_list(user_id=request.session['user_id'],item_id=item_id)
    return redirect('/success')

def delete(request, item_id):
     #ensure user is logged in and redirect if not
    if 'user_id' not in request.session:
           return redirect('/')
   # GET ITEM AND DELETE IT        

    Item.objects.get(id = item_id).delete()

    return redirect(success)

    








