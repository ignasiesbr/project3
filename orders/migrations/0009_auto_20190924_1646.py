# Generated by Django 2.1.5 on 2019-09-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190924_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
