# Generated by Django 3.0.2 on 2020-04-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_profile_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='compositeRating',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='timesTutored',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='timesTutteed',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='tutorRate',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]