# Generated by Django 4.2 on 2023-10-14 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart_coupon_cart_total_after_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='cart',
            new_name='order',
        ),
    ]