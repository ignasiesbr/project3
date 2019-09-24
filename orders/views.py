from django.http import HttpResponse
from django.shortcuts import render
from orders.forms import PizzaForm
from orders.models import *

# Create your views here.
def index(request):
    form = PizzaForm()
    context = {
        "pizzas":Pizza.objects.all(),
        "pastas":Pasta.objects.all(),
        "platters":DinnerPlatter.objects.all(),
        "subs":Sub.objects.all(),
        "salads":Salad.objects.all(),
        "extrasubs":SubExtra.objects.all(),
        "form":form,
        "user":request.user
    }
    return render(request, "orders/index.html", context)

def add_to_cart(request, pasta_id):
    try:
        cart = Cart.objects.get(user_id=request.user.id)
    except:
        cart = Cart(user_id=request.user.id)
        cart.save()
    try:
        pasta = Pasta.objects.get(pk=pasta_id)
    except:
        return render(request, "orders/error.html", {"message":"Article not defined"})

    cart.items.add(pasta)
    context = {
        "items":cart.items.all(),
        "cart":cart
    }
    return render(request, "orders/cart.html", context)
