# Generated by Django 4.2 on 2023-09-28 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_review_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
    ]