# Generated by Django 3.0.2 on 2020-04-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200410_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutee',
            name='ratingPage',
            field=models.CharField(default='', max_length=100),
        ),
    ]
