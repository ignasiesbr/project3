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
        "entries":Entry.objects.filter(cart=my_cart),

    }
    return render(request, "orders/index.html", context)

def add_to_cart(request, super_id):
    if request.method=="GET":
        pasta = Item.objects.get(super_id=super_id)

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

def is_pizza_valid(style, toppings):
    l = []
    for topping in toppings:
        l.append(topping)
    s = str(l[0])
    try:
        n = int(style)
    except ValueError:
        if (style == 'CH' or style== 'SP') and len(l) == 1 and s == "No toppings":
            return True
        else:
            return False

    return n == len(toppings)

def add_pizza_cart(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            style = form.cleaned_data['style']
            size = form.cleaned_data['size']
            extras = form.cleaned_data['extras']
            toppings = form.cleaned_data['toppings']
            quantity = form.cleaned_data['quantity']
            ntoppings = len(toppings)


            # Checks if the style of the pizza corresponds the style
            if is_pizza_valid(extras, toppings):
                pizza = PizzaPrice.objects.filter(type=style, style=extras, size=size)[0]
                item = Item.objects.create(name=str(pizza), price=pizza.price)
                my_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
                try:
                    cart_entries = Entry.objects.filter(cart=my_cart)
                    entry = cart_entries.get(product=pasta)
                    entry.quantity += quantity
                    entry.save()
                    my_cart.total += pizza.price
                    my_cart.count += quantity
                except:
                    entry = Entry.objects.create(product=item,cart=my_cart, quantity=quantity)
                my_cart.save()

                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "orders/error.html", {"message":"MEC"})
