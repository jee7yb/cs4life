# Generated by Django 3.0.2 on 2020-03-01 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200229_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Uid',
            field=models.IntegerField(default=0),
        ),
    ]
