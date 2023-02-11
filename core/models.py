from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# from tinymce.models import HTMLField
from django.shortcuts import reverse
import datetime

# Create your models here.
class ReviewManager(models.Manager):
    def get_queryset(self):
        return super(ReviewManager, self).get_queryset().filter(published=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_review")
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Review manager
    reviews= ReviewManager() # published Review manager

    def __str__(self):
        return str(self.user) + '_review'


class FaqManager(models.Manager):
    def get_queryset(self):
        return super(FaqManager, self).get_queryset().filter(published=True)

class Faq(models.Model):
    question= models.CharField(max_length=350)
    answer = models.TextField()
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Faq manager
    faqs= FaqManager() # published Faq manager
    
    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural= 'Faqs'
        ordering= ('-created_on',)

    def __str__(self):
        return str(self.question) 


class ServiceManager(models.Manager):
    def get_queryset(self):
        return super(ServiceManager, self).get_queryset().filter(published=True)

class Service(models.Model):
    image = models.ImageField(upload_to='core/service/images', blank=True, null= True)
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', default='jcotech services')
    svg_img = models.FileField(upload_to='core/service/svg_img', blank= True, null= True, validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])], help_text='copy and paste the svg image code here' )
    title= models.CharField( max_length=150)
    short_description = models.CharField( max_length=300, default='')
    slug = models.SlugField()
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Service manager
    services= ServiceManager() # published Service manager
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural= 'Services'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title) 
    
    def get_absolute_url(self):
        return reverse( 'core:services', kwargs={'slug':self.slug})


class PortfolioManager(models.Manager):
    def get_queryset(self):
        return super(PortfolioManager, self).get_queryset().filter(published= True)

class Portfolio(models.Model):
    image = models.ImageField( upload_to= 'core/portfolio/images', null=True, blank=True )
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', default= 'image')
    video = models.FileField(upload_to="core/portfolio/videos", null=True, blank=True)
    title= models.CharField( max_length=150)
    content= models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, related_name="project_review", null=True, blank=True)
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default portfolio manager
    portfolios= PortfolioManager() # published portfolio manager
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural= 'Portfolios'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title)


class Position(models.Model):
    name= models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural= 'Positions'
        ordering= ('-created_on',) 
    
    def __str__(self):
        return self.name
    

class OpportunityManager(models.Manager):
    def get_queryset(self):
        return super(OpportunityManager, self).get_queryset().filter(published= True, is_applicant=False)

class Opportunity(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE)
    position = models.ForeignKey(Position, on_delete= models.CASCADE, help_text='select the position you are appling for')
    content= models.TextField(default='')
    portfolio_url= models.URLField(blank=True, null=True, help_text='enter link to your portfolio')
    published= models.BooleanField(default= False)
    is_applicant =models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Opportunity manager
    opportunities= OpportunityManager() # published Opportunity manager

    class Meta:
        verbose_name = 'Opportunity'
        verbose_name_plural= 'Opportunities'
        ordering= ('-created_on',)
    
    def __str__(self):
        return self.content[:150]


STATUS_CHOICE=[('completed','completed'),
('in progress', 'in progress'),
('canceled','canceled'),
('accepted', 'accepted'),
('requested','requested')]

class Quote(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.CharField(max_length=150, default='software in web development')
    upload_file =models.FileField(upload_to='core/quote/files', validators=[FileExtensionValidator(['pdf', 'doc', 'txt'])], help_text="file form must be 'pdf', 'doc' or'txt' ",blank=True, null=True)
    message= models.TextField()
    status=models.CharField(max_length=12, choices=STATUS_CHOICE, default='requested')
    created_on=models.DateTimeField(auto_now_add=True)
    update_on=models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.full_name

class Contact(models.Model):
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message =models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class GallaryManager(models.Manager):
    def get_queryset(self):
        return super(GallaryManager, self).get_queryset().filter(published= True)

class Gallary(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField( upload_to='core/gallary/image', )
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', default= 'image')
    url = models.URLField(blank=True, null=True)
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default gallary manager
    gallaries= GallaryManager() # published gallary manager

    class Meta:
        verbose_name = 'Gallary'
        verbose_name_plural= 'Gallaries'
        ordering= ('-created_on',)

    def __str__(self):
        return str(self.image.url)

    def img_url(self):
        return self.image.url


# event model

class EventManager(models.Manager):
    def get_queryset(self):
        return super(EventManager, self).get_queryset().filter(published=True)

class Event(models.Model):
    title= models.CharField( max_length=150, unique=True)
    keywords = models.CharField(max_length=25, blank=True, null=True)
    short_description = models.CharField( max_length=300, default='')
    slug = models.SlugField(unique=True)
    content = models.TextField(default='')
    url =models.URLField(blank=True, null=True)
    published = models.BooleanField(default=False)
    scheduled_on= models.DateTimeField(default=datetime.datetime.now)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Event manager
    events= EventManager() # published Event manager
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural= 'Events'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title) 
    
    def get_absolute_url(self):
        return reverse( 'core:events', kwargs={'slug':self.slug})

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default='y')
    description =models.TextField()

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField()
    is_subscriber=models.BooleanField(default=True)

    verbose_name = 'subscriber'
    verbose_name_plural='subscribers'

    def __str__(self):
        return self.email

