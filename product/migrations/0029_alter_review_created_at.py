# Generated by Django 4.2 on 2023-09-29 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 19, 10, 59, 535329), verbose_name='created at'),
        ),
    ]
