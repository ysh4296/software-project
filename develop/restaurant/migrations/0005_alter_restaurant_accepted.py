# Generated by Django 3.2.3 on 2021-05-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurant_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='accepted',
            field=models.BooleanField(),
        ),
    ]
