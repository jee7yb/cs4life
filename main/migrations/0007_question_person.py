# Generated by Django 3.0.2 on 2020-04-07 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_profile_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Profile'),
        ),
    ]
