# Generated by Django 4.1.5 on 2023-02-21 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='account/profile_pics/user.svg', upload_to='account/profile_pics')),
                ('about', models.CharField(default='', max_length=300)),
                ('whatsapp_no', models.CharField(blank=True, help_text='enter your whatsapp phone number', max_length=11, null=True)),
                ('telegram_no', models.CharField(blank=True, help_text='enter your telegram phone number', max_length=11, null=True)),
                ('facebook_url', models.URLField(blank=True, help_text='enter your facebook profile url', max_length=150, null=True)),
                ('twitter_url', models.URLField(blank=True, help_text='enter your twitter profile url', max_length=150, null=True)),
                ('instagram_url', models.URLField(blank=True, help_text='enter your instagram profile url', max_length=150, null=True)),
                ('linkedin_url', models.URLField(blank=True, help_text='enter your linkedin profile url', max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
