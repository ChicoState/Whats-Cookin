# Generated by Django 3.2.12 on 2022-05-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0002_auto_20220508_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='date_stocked',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
