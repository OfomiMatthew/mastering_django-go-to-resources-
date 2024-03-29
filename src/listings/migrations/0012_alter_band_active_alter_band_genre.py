# Generated by Django 4.2.7 on 2024-01-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_remove_listing_locale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=''),
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('RB', 'Rythm And Blues'), ('RK', 'Rock'), ('GP', 'Gospel')], default=None, max_length=5),
        ),
    ]
