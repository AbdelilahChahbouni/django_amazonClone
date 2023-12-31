# Generated by Django 4.2 on 2023-08-26 18:44

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 18, 44, 5, 544220, tzinfo=datetime.timezone.utc), verbose_name='created at'),
        ),
    ]
