from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from datetime import datetime


# Create your models here.


 ################ CLIENT REVIEW MODEL ##################
 ################ CLIENT REVIEW MODEL ##################

class ReviewManager(models.Manager):
    def get_queryset(self):
        return super(ReviewManager, self).get_queryset().filter(published=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_review")
    content = models.TextField() 
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Review manager
    reviews= ReviewManager() # custom Review manager

    def __str__(self):
        return str(self.user) + '_review'

 
 
 ################ FAQ MODEL ##################
 ################ FAQ MODEL ##################

class FaqManager(models.Manager):
    def get_queryset(self):
        return super(FaqManager, self).get_queryset().filter(published=True)

class Faq(models.Model):
    question= models.CharField(max_length=350)
    answer = models.TextField()
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Faq manager
    faqs= FaqManager() # custom Faq manager
    
    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural= 'Faqs'
        ordering= ('-created_on',)

    def __str__(self):
        return str(self.question) 



 ################ SERVICE MODEL ##################
 ################ SERVICE MODEL ##################

class ServiceManager(models.Manager):
    def get_queryset(self):
        return super(ServiceManager, self).get_queryset().filter(published=True)

class Service(models.Model):
    svg_img = models.FileField(upload_to='core/service/svg_img', blank= True, null= True, validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])], help_text='copy and paste the svg image code here' )
    title= models.CharField( max_length=150)
    keywords = models.CharField( max_length=100, blank=True, null=True, help_text="enter comma separated words")
    short_description = models.CharField( max_length=160, default='')
    slug = models.SlugField()
    content = HTMLField()
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Service manager
    services= ServiceManager() # custom Service manager
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural= 'Services'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title) 
    
    def get_absolute_url(self):
        return reverse( 'core:services', kwargs={'slug':self.slug})



 ################ PORTFOLIO_CAT MODEL ##################
 ################ PORTFOLIO_CAT MODEL ##################

class PortfolioCatManager(models.Manager):
    def get_queryset(self):
        return super(PortfolioCatManager, self).get_queryset().filter(published= True)

class PortfolioCat(models.Model):
    title=models.CharField(max_length=50)
    slug = models.SlugField(default='')
    image=models.ImageField(upload_to='core/portfolio/category_img')
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', null=True, blank=True, default= '')
    published=models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    
    objects=models.Manager() #default portfolio manager
    portfolio_cats= PortfolioCatManager() # custom portfolio manager
    
    class Meta:
        verbose_name = 'PortfolioCat'
        verbose_name_plural= 'PortfolioCats'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse( 'core:project')+'?category='+self.slug



 ################ PORTFOLIO MODEL ##################
 ################ PORTFOLIO MODEL ##################

class PortfolioManager(models.Manager):
    def get_queryset(self):
        return super(PortfolioManager, self).get_queryset().filter(published= True)

class Portfolio(models.Model):
    image = models.ImageField( upload_to= 'core/portfolio/images', null=True, blank=True )
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image ', null=True, blank=True)
    keywords =models.CharField(max_length=100, blank=True, null=True, help_text="enter comma separated words")
    short_description = models.CharField( max_length=160, default='')
    video = models.FileField(upload_to="core/portfolio/videos", null=True, blank=True)
    title= models.CharField( max_length=150)
    slug = models.SlugField(default='')
    category= models.ForeignKey(PortfolioCat, on_delete=models.SET_NULL, null=True, default='')
    content= HTMLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, related_name="project_review", null=True, blank=True)
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default portfolio manager
    portfolios= PortfolioManager() # custom portfolio manager
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural= 'Portfolios'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse( 'core:project', kwargs={'slug':self.slug})



 ################ EVENT_CAT MODEL ##################
 ################ EVENT_CAT MODEL ##################

class EventCatManager(models.Manager):
    def get_queryset(self):
        return super(EventCatManager, self).get_queryset().filter(published= True)

class EventCat(models.Model):
    title=models.CharField(max_length=50)
    slug = models.SlugField(default='')
    image=models.ImageField(upload_to='core/event/category_img')
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', null=True, blank=True, default= '')
    published=models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    
    objects=models.Manager() #default event manager
    event_cats= EventCatManager() # custom event manager
    
    class Meta:
        verbose_name = 'EventCat'
        verbose_name_plural= 'EventCats'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse( 'core:event')+'?category='+self.slug



 ################ EVENT MODEL ##################
 ################ EVENT MODEL ##################

class EventManager(models.Manager):
    def get_queryset(self):
        return super(EventManager, self).get_queryset().filter(published=True)

class Event(models.Model):
    image = models.ImageField(upload_to='core/event', default='')
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', null=True, blank=True)
    title= models.CharField( max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    keywords = models.CharField(max_length=100, blank=True, null=True, help_text="enter comma separated words")
    short_description = models.CharField( max_length=160, default='')
    content = HTMLField(default='')
    category = models.ForeignKey(EventCat, on_delete=models.SET_NULL, null=True, default='')
    url =models.URLField(blank=True, null=True)
    published = models.BooleanField(default=False)
    scheduled_on= models.DateTimeField(default=datetime.now)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Event manager
    events= EventManager() # custom Event manager
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural= 'Events'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title) 
    
    def get_absolute_url(self):
        return reverse( 'core:event_details', kwargs={'slug':self.slug})




 


 ################ OPPORTUNITY POSITION  MODEL ##################
 ################ OPPORTUNITY POSITION  MODEL ##################

class Position(models.Model):
    name= models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural= 'Positions'
        ordering= ('-created_on',) 
    
    def __str__(self):
        return self.name
    


 ################ OPPORTUNITY MODEL ##################
 ################ OPPORTUNITY MODEL ##################

class OpportunityManager(models.Manager):
    def get_queryset(self):
        return super(OpportunityManager, self).get_queryset().filter(published= True, is_applicant=False)

class Opportunity(models.Model):
    user= models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True )
    full_name = models.CharField(max_length=25, default='')
    salary = models.CharField(default='Negotiable', max_length=10)
    job_type = models.CharField(choices=[('full time','Full Time'), ('Part Time / B2B Contract',"Part Time / B2B Contract")], max_length=24, default="'Part Time / B2B Contract'")
    position = models.ForeignKey(Position, on_delete= models.CASCADE, help_text='select the position you are applying for')
    location = models.CharField(max_length=300, default="Remotely")
    details= HTMLField(default='', help_text="should contain job description and skils required")
    portfolio_url= models.URLField(blank=True, null=True, help_text='enter link to your portfolio')
    published= models.BooleanField(default= False)
    is_applicant =models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default Opportunity manager
    opportunities= OpportunityManager() # custom Opportunity manager

    class Meta:
        verbose_name = 'Opportunity'
        verbose_name_plural= 'Opportunities'
        ordering= ('-created_on',)
    
    def __str__(self):
        return str(self.position)



 ################ QUOTE MODEL ##################
 ################ QUOTE MODEL ##################

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
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.full_name



 ################ CONTACT MODEL ##################
 ################ CONTACT MODEL ##################

class Contact(models.Model):
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField()
    phone= models.CharField(default='', max_length=15)
    subject = models.CharField(max_length=255)
    message =models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email



 ################ GALLARY MODEL ##################
 ################ GALLARY MODEL ##################

class GallaryManager(models.Manager):
    def get_queryset(self):
        return super(GallaryManager, self).get_queryset().filter(published= True)

class Gallary(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField( upload_to='core/gallary/image', )
    caption=models.CharField(max_length=50, default='', help_text="give a name for this image")
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default gallary manager
    gallaries= GallaryManager() # custom gallary manager

    class Meta:
        verbose_name = 'Gallary'
        verbose_name_plural= 'Gallaries'
        ordering= ('-created_on',)

    def __str__(self):
        return str(self.image.url)

    def img_url(self):
        return self.image.url


   
 ################ SUBSCRIBER MODEL ##################
 ################ SUBSCRIBER MODEL ##################

class SubscriberManager(models.Manager):
    def get_queryset(self):
        return super(SubscriberManager, self).get_queryset().filter(verify_email=True)
class Subscriber(models.Model):
    email = models.EmailField()
    is_subscriber=models.BooleanField(default=True)
    verified_email =models.BooleanField(default=False)
    subscribed_on = models.DateTimeField(default=datetime.now)

    objects=models.Manager() #default Subscriber manager
    subscribers= EventManager() # custom Subscriber manager

    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural='subscribers'
        ordering= ('-subscribed_on',)

    def __str__(self):
        return self.email






################ PRIVACY / POLICY MODEL ##################
 ################ PRIVACY / POLICY MODEL ##################

class PrivacyPolicyManager(models.Manager):
    def get_queryset(self):
        return super(PrivacyPolicyManager, self).get_queryset().filter(published=True)

class PrivacyPolicy(models.Model):
    image = models.ImageField(upload_to='core/privacy_policy', default='', blank=True, null=True)
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', null=True, blank=True)
    title= models.CharField( max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    content = HTMLField(default='')
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default PrivacyPolicy manager
    p_ps = PrivacyPolicyManager() # custom PrivacyPolicy manager
    
    class Meta:
        verbose_name = 'PrivacyPolicy'
        verbose_name_plural= 'PrivacyPolicies'
        ordering= ('-created_on',) 

    def __str__(self):
        return str(self.title) 
    
    