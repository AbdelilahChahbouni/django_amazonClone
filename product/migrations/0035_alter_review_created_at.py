# Generated by Django 4.2 on 2023-09-29 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default='2023-09-29 19:30:01', verbose_name='created at'),
        ),
    ]