from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from tinymce.models import HTMLField
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.



 ################ CAATEGORY  MODEL ##################
 ################ CAATEGORY  MODEL ##################

class CategoryManager(models.Manager):
    def get_queryset(self):
        return super(CategoryManager, self).get_queryset().filter(is_published=True)
class Category(models.Model):
    title=models.CharField(max_length = 255, unique=True)
    slug =models.SlugField(max_length=255)
    created      = models.DateField(auto_now_add=True) 
    updated      = models.DateField('last updated', auto_now=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
    objects=models.Manager() #default article manager
    categories=CategoryManager() #custom article manager

    def get_absolute_url(self):
        return reverse('blog:articles')+ '?category='+self.slug

 ################ TAG  MODEL ##################
 ################ TAG  MODEL ##################

class Tag(models.Model):
    title=models.CharField(max_length = 255, unique=True)
    slug =models.SlugField(max_length=255)
    created      = models.DateField(auto_now_add=True) 
    updated      = models.DateField('last updated', auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Tag"
        verbose_name_plural="Tags"

    def get_absolute_url(self):
        return reverse('blog:articles')+ '?tag='+self.slug

def user_directory_path(instance, filename):
    return "posts/{0}/{1}".format(instance,filename)



 ################ ARTICLE  MODEL ##################
 ################ ARTICLE  MODEL ##################

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(is_published=True, is_approved=True)

class Article(models.Model):
    title             = models.CharField(max_length=150, unique=True)
    slug               = models.SlugField(max_length=150, unique=True )
    header_image        = models.ImageField(upload_to='blog/header_images')
    alt_text = models.CharField(
        verbose_name=("alt text"),
        help_text=("Please add alternate text. this text gets displayed when the image fails to load on time"),
        max_length=50,
        null=True,
        blank=True,
    )
    author            = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video              =models.URLField(blank=True, null=True, help_text='when adding a video url ensure to check the \'is_video\' \
    field and add video description in content field. Also upload an image to be use as thumbnail')
    short_description       = models.CharField( max_length=160, help_text='give a short description in not more than 160 chars. this will help users find your post on search engines')
    keywords = models.CharField(max_length=100, help_text="enter comma separated words")
    content = HTMLField(help_text='use this field as video description when providing video url')
    category          = models.ForeignKey(Category, max_length=50,related_name='category_articles', on_delete=models.SET_NULL, null= True )
    tags               = models.ManyToManyField(Tag, related_name='tags', blank=True)
    love             = models.ManyToManyField(Profile,  related_name='love', blank=True )
    is_video            = models.BooleanField(default=False)
    is_featured         = models.BooleanField(default=False)
    is_reviewed         = models.BooleanField(default=False)
    is_sponsored       = models.BooleanField(default=False)
    is_published       = models.BooleanField(default=True)
    is_approved         = models.BooleanField(default=False)
    created     = models.DateField(auto_now_add=True) 
    updated      = models.DateField('last updated', auto_now=True)

  
    objects = models.Manager() #default article manager
    articles = ArticleManager() #custom article manager

    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
        ordering=["-created",]
    def __str__(self):
        return self.title

    def total_love(self):
        return self.love.count()

    def total_share(self):
        shares=Share.objects.filter(article=self).count()
        return shares

    def total_views(self):
        views=Viewer.objects.filter(article=self).count()
        distinct_views = Viewer.objects.filter(article=self).distinct().count()
        return str(views) + " "+ "("+str(distinct_views)+")d"

    def secrete():
        print(secrete.tokens_urlsafe)

    def author_name(self):
        if self.author.user.first_name:
            full_name = self.author.user.first_name+ " " + self.author.user.last_name
        else:
            full_name=self.author.user.username
        return full_name
    
    def get_absolute_url(self): 
        return reverse_lazy('blog:article_details', args=[self.slug])



 ################ COMMENT  MODEL ##################
 ################ COMMENT  MODEL ##################

class Comment(models.Model):
    user       =   models.ForeignKey(User, on_delete=models.CASCADE)
    article        =   models.ForeignKey(Article,  on_delete = models.CASCADE)
    content         =   models.TextField()
    love   =   models.ManyToManyField(User, related_name='love_comment',  blank=True )
    parent              = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,related_name='replies')
    created      = models.DateTimeField(auto_now_add=True) 
    updated      = models.DateTimeField(auto_now=True)
    is_published       = models.BooleanField(default=True)

    class Meta:
        ordering=['-created']
    
    def now_plus_30(): 
        return datetime.now() + timedelta(days = 30) 
    
    def get_parent(self):
        if not self.parent :
            return True
        return False
    
    def get_children(self):
        return Comment.objects.filter(parent=self).reverse()       
       
    def total_love(self):
        return self.love.count()
    def __str__(self):
        return str(self.user)  +' __'  + str(self.article)



 ################ SHARE  MODEL ##################
 ################ SHARE  MODEL ##################

SOCIALS=(
        ('facebook', 'facebook'),
        ('linkedin', 'linkedin'),
        ('twitter', 'twitter'),
        ('whatsapp', 'whatsapp'),
        ('telegram', 'telegram'),
    )

class Share(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    social_medium =models.CharField(choices=SOCIALS, max_length=10)
    shared_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'share'
        verbose_name_plural= 'shares'



 ################ VIEWER  MODEL ##################
 ################ VIEWER  MODEL ##################

class Viewer(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip=models.CharField(max_length=50)
    # view_count = models.PositiveIntegerField(default=0)
    viewed_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ip  



        # .filter((Q(for_field__is_null=True) | Q(for_field__bool=True))
# use the line of  code above to check for field with the field name first and the filter attribute second for multiple filtering of a foreign key






# copied and pasted chatgpt stuff
# models.py

# from django.db import models

# class Property(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

# class Block(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)


# views.py

# from django.shortcuts import render
# from .models import Property, Block

# def property_list(request):
#     properties = Property.objects.all()
#     return render(request, 'property_list.html', {'properties': properties})

# def property_detail(request, pk):
#     property = Property.objects.get(pk=pk)
#     return render(request, 'property_detail.html', {'property': property})

# def block_list(request):
#     blocks = Block.objects.all()
#     return render(request, 'block_list.html', {'blocks': blocks})

# def block_detail(request, pk):
#     block = Block.objects.get(pk=pk)
#     return render(request, 'block_detail.html', {'block': block})


# # urls.py

# from django.urls import path
# from .views import property_list, property_detail, block_list, block_detail

# urlpatterns = [    path('properties/', property_list, name='property_list'),    path('properties/<int:pk>/', property_detail, name='property_detail'),    path('blocks/', block_list, name='block_list'),    path('blocks/<int:pk>/', block_detail, name='block_detail'),]


# templates

# <!-- property_list.html -->
# {% extends 'base.html' %}

# {% block content %}
#   <h1>Properties</h1>
#   {% for property in properties %}
#     <h2>{{ property.name }}</h2>
#     <p>{{ property.description }}</p>
#     <p>Price: ${{ property.price }}</p>
#     <a href="{% url 'property_detail' property.pk %}">View details</a>
#   {% endfor %}
# {% endblock %}

# <!-- property_detail.html -->
# {% extends 'base.html' %}

# {% block content %}
#   <h1>{{ property.name }}</h1>
#   <p>{{ property.description }}</p>
#   <p>Address: {{ property.address }}, {{ property.city }}, {{ property.state }}, {{ property.country }}</p>
#   <p>Price: ${{ property.price }}</p>
# {% endblock %}

# <!-- block_list.html -->
# {% extends 'base.html' %}

# {% block content %}
#   <h1>Blocks</h1>
#   {% for block in blocks %}
#     <h2>{{ block.name }}</h2>
#     <p>{{ block.description }}</p>
#     <p>Price: ${{ block.price }}</p>
#     <a href="{% url 'block_detail' block.pk %}">View details</a>
#   {% endfor %}
# {% endblock %}

# <!-- block_detail.html -->
# {% extends 'base.html' %}

# {% block content %}
#   <h1>{{ block.name }}</h1>
#   <p>{{ block.description }}</p>
#   <p>Price: ${{ block.price }}</p>
# {% endblock %}
