from django.forms import ModelForm, ModelMultipleChoiceField
from orders.models import PizzaOrder
from django import forms
from orders.models import Topping


class PizzaForm(ModelForm):
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all())
    class Meta:
        model = PizzaOrder
        fields = ['style', 'size', 'extras', 'toppings', 'quantity']
