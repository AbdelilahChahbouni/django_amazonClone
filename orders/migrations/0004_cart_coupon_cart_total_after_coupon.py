# Generated by Django 4.2 on 2023-10-14 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_cartdetail_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_coupon', to='orders.coupon'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_after_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
