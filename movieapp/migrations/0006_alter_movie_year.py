# Generated by Django 4.2.6 on 2023-10-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
