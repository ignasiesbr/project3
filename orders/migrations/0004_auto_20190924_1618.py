# Generated by Django 2.1.5 on 2019-09-24 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190924_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cart'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pasta'),
        ),
    ]
