from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
   return render(request,'amadon_app/index.html')

def buy(request):
  price = {
    "101" : 19.99,
    "201" : 29.99,
    "301" : 4.99,
    "401" : 49.99
  }
  quantity = request.POST['quantity'] 
  product = request.POST['product_id']
  request.session["total_price"] = int(quantity)* price[product]

  if "total_purchase" not in request.session:
    request.session["total_purchase"] = request.session["total_price"]
    request.session["item"] = int(quantity)
  else:
    request.session["total_purchase"] += request.session["total_price"]
    request.session["item"] += int(quantity)

  return redirect('/amadon/checkout')

def checkout(request):
  return render(request,'amadon_app/checkout.html')

def back(request):
    return redirect('/')  

    
   