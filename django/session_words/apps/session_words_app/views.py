from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if "word_list" not in request.session:
        request.session["word_list"] = []


    print(request.session['word_list'])
    return render(request, "session_words_app/index.html")

def processform(request):
    print(request.POST) #to print all form


    new_word = {
        "word": request.POST["word"],
        "color": request.POST["color"],
        "font": request.POST["font"]
    }
    #temp_list = request.session['word_list']
    #temp_list.append(new_word)
    #request.session['word_list'] = temp_list
    request.session["word_list"].append(new_word)
    request.session.modified = True
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')  



