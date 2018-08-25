from django.shortcuts import render,HttpResponse,redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request,'random_word_app/index.html')

def random_word(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    words = {
        'word':get_random_string(length=14)
    }
    return render(request, 'random_word_app/index.html',words)    

def reset(request):
    request.session.clear()
    return redirect('/')        

# Create your views here.
