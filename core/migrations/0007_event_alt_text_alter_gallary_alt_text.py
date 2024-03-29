# Generated by Django 4.1.5 on 2023-03-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_event_image_alter_portfoliocat_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='alt_text',
            field=models.CharField(blank=True, help_text='enter an alternate text for this image', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='gallary',
            name='alt_text',
            field=models.CharField(blank=True, help_text='enter an alternate text for this image', max_length=50, null=True),
        ),
    ]
