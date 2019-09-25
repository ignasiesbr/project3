from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from orders.forms import PizzaForm, SubForm
from orders.models import *
from django.db import models
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == "POST":
        return render(request, "orders/error.html",{"message":"POST request method not allowed"})
    if request.user.is_authenticated:
        form = PizzaForm()
        sub_form = SubForm()
        my_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
        context = {
            "pizzas":Pizza.objects.all(),
            "pastas":Pasta.objects.all(),
            "platters":DinnerPlatter.objects.all(),
            "subs":Sub.objects.all(),
            "salads":Salad.objects.all(),
            "extrasubs":SubExtra.objects.all(),
            "form":form,
            "sub_form":sub_form,
            "user":request.user,
            "cart":my_cart,
            "entries":Entry.objects.filter(cart=my_cart),

        }
        return render(request, "orders/index.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))

def retrieveCart(request):
    my_cart, created = Cart.objects.get_or_create(user_id=request.user.id)
    return my_cart

def updateCart(item, cart, quantity):
    cart.total += item.price
    cart.count += quantity
    cart.save()

def createEntry(item, cart, quantity):
    try:
        cart_entries = Entry.objects.filter(cart=cart)
        entry = cart_entries.get(product=item)
        entry.quantity += quantity
        entry.save()
        updateCart(item, cart, quantity)
    except:
        entry = Entry.objects.create(product=item, cart=cart, quantity=quantity)
    cart.save()


def add_to_cart(request, super_id):
    if request.method=="GET":
        item = Item.objects.get(super_id=super_id)

        my_cart = retrieveCart(request)
        createEntry(item, my_cart, 1)

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
                my_cart = retrieveCart(request)
                createEntry(item, my_cart, quantity)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "orders/error.html", {"message":"MEC"})

def createSubItem(sub, extras):
    if str(extras[0]) == "No extras - $0.00":
        item = Item.objects.create(name=str(sub), price=sub.price)
    else:
        str_extras = ""
        price_extras = 0
        for extra in extras:
            str_extras += str(extra)
            price_extras += extra.price
        str_sub = str(sub) + " Extras: " + str_extras
        total_price = sub.price + price_extras
        item = Item.objects.create(name=str_sub, price=total_price)

    return item

def add_sub_cart(request):

    if request.method == "POST":
        form = SubForm(request.POST)

        if form.is_valid():
            sub = form.cleaned_data['subs']
            extras = form.cleaned_data['extras']
            my_cart = retrieveCart(request)
            item = createSubItem(sub, extras)
            createEntry(item, my_cart, 1)

            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/error.html", {"message":"aqui estem"})


def reset_cart(request):
    my_cart = retrieveCart(request)
    my_cart.delete()
    my_cart = retrieveCart(request)
    return HttpResponseRedirect(reverse("index"))
