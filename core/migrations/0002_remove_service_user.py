# Generated by Django 4.1.5 on 2023-01-25 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='user',
        ),
    ]
