from django.db import models
from django.utils.datetime_safe import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

SIZES = (
    ("S", "SMALL"),
    ("L", "LARGE")
)

STYLES = (
    ("R", "REGULAR"),
    ("S", "SICILIAN")
)

# Create your models here.

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length=10, choices=SIZES)

    def __str__(self):
        return f"{self.name} - ${self.price} - size: {self.size}"

class SubExtra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=10, choices=SIZES)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    extra = models.ManyToManyField(SubExtra, blank=True)

    def __str__(self):
        return f"{self.name} - ${self.price} - size: {self.size}"

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    style = models.CharField(max_length=64, choices=STYLES)
    size = models.CharField(max_length=64, choices=SIZES)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return f"{self.get_style_display()} - {self.get_size_display()} - {self.price} - Toppings: {self.toppings.in_bulk()}"


class PizzaOrder(Pizza):
    CHOICES = (
        ('CH', 'Cheese'),
        ('1', '1 Topping'),
        ('2', '2 Toppings'),
        ('3', '3 Toppings'),
        ('SP', 'Special')
    )

    style = Pizza.style
    size = Pizza.size
    extras = models.CharField(max_length=15 ,choices=CHOICES, default='CH')
    toppings = Pizza.toppings

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.get_style_display()} - {self.get_size_display()}"

class Cart(models.Model):
    user_id = models.IntegerField()
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
"""
    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user_id, self.count, self.total)
"""
class Entry(models.Model):
    product = models.ForeignKey(Pasta, null=True, on_delete='CASCADE')
    cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.name)


@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.product.price
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = datetime.now()
