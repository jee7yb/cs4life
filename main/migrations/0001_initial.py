# Generated by Django 3.0.2 on 2020-02-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_text', models.CharField(max_length=200)),
                ('Class_text', models.CharField(max_length=200)),
                ('Comments_text', models.CharField(max_length=10000)),
                ('File_upload', models.ImageField(upload_to='')),
            ],
        ),
    ]
