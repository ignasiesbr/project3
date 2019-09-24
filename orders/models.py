from django.db import models

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
    items = models.ManyToManyField(Pasta, related_name="cart", null=True, blank=True)
