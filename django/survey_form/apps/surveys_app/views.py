from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request,'surveys_app/index.html')


def process(request):
    request.session['counter'] += 1
    print(request.POST)
    print(request.POST['name'])
    print(request.POST['location'])
    print(request.POST['language'])
    print(request.POST['comments'])

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect('/result')

def clear(request):
    request.session.clear()
    return redirect('/')


def result(request):
    return render(request,'surveys_app/result.html')
