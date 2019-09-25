from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/<int:super_id>", views.add_to_cart, name="add_to_cart"),
    path("cart/add_pizza", views.add_pizza_cart, name="add_pizza_cart")
]
