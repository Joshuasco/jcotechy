from django.db import models

# Create your models here.
# import uuid

from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account/profile_pics', default='account/profile_pics/user.svg')
    whatsapp_no     =models.CharField(max_length=11,  blank=True, null=True, help_text='enter your whatsapp phone number')
    telegram_no     =models.CharField(max_length=11,  blank=True, null=True, help_text='enter your telegram phone number' )
    facebook_url   = models.URLField(max_length=150, blank=True, null=True, help_text='enter your facebook profile url')
    twitter_url     = models.URLField(max_length=150, blank=True, null=True, help_text='enter your twitter profile url')
    instagram_url  = models.URLField(max_length=150, blank=True, null=True, help_text='enter your instagram profile url')
    linkedin_url     = models.URLField(max_length=150, blank=True, null=True, help_text='enter your linkedin profile url')
    def __str__(self):
        return self.user.username


def profile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)

def save_profile_receiver(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(profile_receiver, sender=User)
post_save.connect(save_profile_receiver, sender=User)