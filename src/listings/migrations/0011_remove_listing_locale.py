# Generated by Django 4.2.7 on 2024-01-10 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_listing_locale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='locale',
        ),
    ]
