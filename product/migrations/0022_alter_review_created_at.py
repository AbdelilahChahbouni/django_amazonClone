# Generated by Django 4.2 on 2023-09-28 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 28, 22, 5, 6, 141681, tzinfo=datetime.timezone.utc), verbose_name='created at'),
        ),
    ]
