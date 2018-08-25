# Create your views here.
from django.shortcuts import  render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def show(request, number):
    return HttpResponse("placeholder to display blog {}".format(number))  

def create(request):
   return redirect('/') #(('/otherpage)if wants to redirect to other page)

def edit(request, number):
    return HttpResponse("display 'placeholder to edit blog {}".format(number))
    
def destroy(request,number):
    return redirect('/')  