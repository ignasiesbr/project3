from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/<int:pasta_id>", views.add_to_cart, name="add_to_cart")
]
