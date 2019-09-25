from django.forms import ModelForm, ModelMultipleChoiceField
from orders.models import PizzaOrder, Sub, SubExtra
from django import forms
from orders.models import Topping


class PizzaForm(ModelForm):
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all())
    class Meta:
        model = PizzaOrder
        fields = ['style', 'size', 'extras', 'toppings', 'quantity']

class SubForm(ModelForm):
    subs = forms.ModelChoiceField(queryset=Sub.objects.all())
    extras = forms.ModelMultipleChoiceField(queryset=SubExtra.objects.all())
    class Meta:
        model = Sub
        fields = ['subs','extras']
