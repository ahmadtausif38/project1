# Generated by Django 3.2.3 on 2021-09-18 17:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_cart_customer_orderplaced'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
