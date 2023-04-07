# Generated by Django 4.1.5 on 2023-03-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='is_event',
            new_name='is_approved',
        ),
        migrations.RemoveField(
            model_name='article',
            name='is_product',
        ),
        migrations.RemoveField(
            model_name='article',
            name='is_project',
        ),
        migrations.AlterField(
            model_name='article',
            name='alt_text',
            field=models.CharField(blank=True, help_text='Please add alturnative text. this text gets displayed when the image fails to load on time', max_length=50, null=True, verbose_name='alt text'),
        ),
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.CharField(default='', help_text='enter comma separated words', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=models.CharField(default='', help_text='give a short description in not more than 225 words. this will help users find your post on search engines', max_length=160),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]