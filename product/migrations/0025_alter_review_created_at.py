# Generated by Django 4.2 on 2023-09-29 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=datetime.timezone.utc), verbose_name='created at'),
        ),
    ]
