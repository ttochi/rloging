# Generated by Django 4.0.4 on 2022-05-25 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='real_name',
        ),
    ]
