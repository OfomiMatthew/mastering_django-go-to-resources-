# Generated by Django 4.2.7 on 2024-01-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_description_listing_sold_listing_types_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('RB', 'Rythm And Blues'), ('RK', 'Rock'), ('GP', 'Gospel')], default='', max_length=5),
        ),
    ]
