from django.http import HttpResponse
from django.shortcuts import render
from orders.forms import PizzaForm
from orders.models import *
from django.db.models import F
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
    pasta = Pasta.objects.get(id=pasta_id)
    try:
        my_cart = Cart.objects.get(user_id=request.user.id)
    except Cart.DoesNotExist:
        my_cart = Cart.objects.create(user_id=request.user.id)
        my_cart.save()

    try:
        entry = Entry.objects.get(cart=my_cart)
    except Entry.DoesNotExist:
        entry = Entry.objects.create(product=pasta, cart=my_cart, quantity=1)


        


    return render(request, "orders/cart.html", )
