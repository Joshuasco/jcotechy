# Generated by Django 4.1.5 on 2023-03-23 11:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_alt_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_medium', models.CharField(choices=[('facebook', 'facebook'), ('linkedin', 'linkedin'), ('twitter', 'twitter'), ('whatsapp', 'whatsapp'), ('telegram', 'telegram')], max_length=10)),
                ('shared_date', models.DateTimeField(default=datetime.datetime.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
            options={
                'verbose_name': 'share',
                'verbose_name_plural': 'shares',
            },
        ),
        migrations.DeleteModel(
            name='Block',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
