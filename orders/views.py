from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from orders.forms import PizzaForm
from orders.models import *
from django.db.models import F
from django.db import models
from django.urls import reverse
# Create your views here.
def index(request):
    form = PizzaForm()
    my_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
    context = {
        "pizzas":Pizza.objects.all(),
        "pastas":Pasta.objects.all(),
        "platters":DinnerPlatter.objects.all(),
        "subs":Sub.objects.all(),
        "salads":Salad.objects.all(),
        "extrasubs":SubExtra.objects.all(),
        "form":form,
        "user":request.user,
        "cart":my_cart,
        "entries":Entry.objects.filter(cart=my_cart)
    }
    return render(request, "orders/index.html", context)

def add_to_cart(request, pasta_id):
    pasta = Pasta.objects.get(id=pasta_id)

    my_cart, created = Cart.objects.get_or_create(user_id=request.user.id)

    try:
        cart_entries = Entry.objects.filter(cart=my_cart)
        entry = cart_entries.get(product=pasta)
        entry.quantity += 1
        entry.save()
        my_cart.total += pasta.price
        my_cart.count += 1
    except:
        entry = Entry.objects.create(product=pasta, cart=my_cart, quantity=1)

    my_cart.save()

    return HttpResponseRedirect(reverse("index"))
