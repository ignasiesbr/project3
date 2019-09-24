# Generated by Django 2.1.5 on 2019-09-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('size', models.CharField(choices=[('S', 'SMALL'), ('L', 'LARGE')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('R', 'REGULAR'), ('S', 'SICILIAN')], max_length=64)),
                ('size', models.CharField(choices=[('S', 'SMALL'), ('L', 'LARGE')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('size', models.CharField(choices=[('S', 'SMALL'), ('L', 'LARGE')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='SubExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('pizza_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Pizza')),
                ('extras', models.CharField(choices=[('CH', 'Cheese'), ('1', '1 Topping'), ('2', '2 Toppings'), ('3', '3 Toppings'), ('SP', 'Special')], default='CH', max_length=15)),
                ('quantity', models.IntegerField(default=1)),
            ],
            bases=('orders.pizza',),
        ),
        migrations.AddField(
            model_name='sub',
            name='extra',
            field=models.ManyToManyField(blank=True, to='orders.SubExtra'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='orders.Topping'),
        ),
    ]