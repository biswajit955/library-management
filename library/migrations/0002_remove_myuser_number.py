# Generated by Django 4.0.5 on 2022-07-18 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='Number',
        ),
    ]
