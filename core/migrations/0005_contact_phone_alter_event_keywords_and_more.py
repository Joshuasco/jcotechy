# Generated by Django 4.1.5 on 2023-03-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_subscriber_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='event',
            name='keywords',
            field=models.CharField(blank=True, help_text='enter comma separated words', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='alt_text',
            field=models.CharField(blank=True, help_text='enter an alternate text for this image ', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='keywords',
            field=models.CharField(blank=True, help_text='enter comma separated words', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='short_description',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AlterField(
            model_name='product',
            name='keywords',
            field=models.CharField(blank=True, help_text='enter comma separated words', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='keywords',
            field=models.CharField(blank=True, help_text='enter comma separated words', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='short_description',
            field=models.CharField(default='', max_length=160),
        ),
    ]