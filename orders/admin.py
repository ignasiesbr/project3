from django.contrib import admin
from orders.models import *

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Sub)
admin.site.register(SubExtra)
admin.site.register(PizzaOrder)
admin.site.register(Cart)
admin.site.register(Entry)
admin.site.register(PizzaPrice)
