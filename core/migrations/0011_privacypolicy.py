# Generated by Django 4.1.5 on 2023-04-07 02:17

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_eventcat_event_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='core/privacy_policy')),
                ('alt_text', models.CharField(blank=True, help_text='enter an alternate text for this image', max_length=50, null=True)),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', tinymce.models.HTMLField(default='')),
                ('published', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'PrivacyPolicy',
                'verbose_name_plural': 'PrivacyPolicies',
                'ordering': ('-created_on',),
            },
        ),
    ]
