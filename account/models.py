from django.db import models
import uuid
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Profile(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account/profile_pics', default='account/profile_pics/user.svg')
    about= models.CharField(max_length=300, default='')
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

CHOICES= [
    ('NN', 'None'),
    ('SA', 'Shipping Address'),
    ('BA', 'Billing Address'),
]

class Address(models.Model):
    """
    Address
    """
    user = models.ForeignKey(User, verbose_name=_("Customer"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.CharField(_("Phone Number"), max_length=15)
    address = models.CharField(_("Address"),max_length=150)
    country= models.CharField(_("Country"), max_length=50 )
    state= models.CharField(_("State"), max_length=50, blank=True, null=True)
    town_city = models.CharField(_("City"), max_length=50, blank=True, null=True )
    street = models.CharField(_("Street"), max_length=50)
    postcode = models.PositiveIntegerField(_("Postcode"))
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    address_type =models.CharField(_("Address Type"), choices=CHOICES, max_length=2, default="NN")
    default = models.BooleanField(_("Set as Default "), default=False)
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = ['-updated_on']

    def __str__(self):
        if self.address_type == "BA":
            return "Address_" + "Billing"
        if self.address_type == "SA":
            return "Address_" + "Shipping"