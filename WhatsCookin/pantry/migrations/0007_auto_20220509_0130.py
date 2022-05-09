# Generated by Django 3.2.12 on 2022-05-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0006_auto_20220509_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fridge',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='fridge',
            name='ingredient',
            field=models.ManyToManyField(to='pantry.Ingredient'),
        ),
    ]
