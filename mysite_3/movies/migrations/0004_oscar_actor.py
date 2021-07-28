# Generated by Django 3.2.5 on 2021-07-08 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_country_movie_oscar'),
    ]

    operations = [
        migrations.AddField(
            model_name='oscar',
            name='actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oscars', to='movies.actor'),
        ),
    ]
