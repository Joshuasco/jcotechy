from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from tinymce.models import HTMLField
# from tinymce.models import HTMLField  should be replaced with ckeditor
# Create your models here.
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

def user_directory_path(instance, filename):
    return "posts/{0}/{1}".format(instance,filename)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(is_published=True)

class Article(models.Model):
    title             = models.CharField(max_length=255, unique=True)
    slug               = models.SlugField(max_length=255, unique=True )
    header_image        = models.ImageField(upload_to='blog/header_images')
    alt_text = models.CharField(
        verbose_name=("Alturnative text"),
        help_text=("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    author            = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video              =models.URLField(blank=True, null=True, help_text='when adding a video url ensure to check the \'is_video\' \
    field and add video description in content field. Also upload an image to be use as thumbnail')
    content           = HTMLField()
    category          = models.ForeignKey(Category, max_length=50,related_name='category_articles', on_delete=models.SET_NULL, null= True )
    tags               = models.ManyToManyField(Tag, related_name='tags', blank=True)
    love             = models.ManyToManyField(Profile,  related_name='love', blank=True )
    is_video            = models.BooleanField(default=False)
    is_featured         = models.BooleanField(default=False)
    is_sponsored       = models.BooleanField(default=False)
    is_project          = models.BooleanField(default=False)
    is_event            = models.BooleanField(default=False)
    is_product          = models.BooleanField(default=False)
    is_published       = models.BooleanField(default=True)
    created     = models.DateField(auto_now_add=True) 
    updated      = models.DateField('last updated', auto_now=True)

  
    objects=models.Manager() #default article manager
    articles = ArticleManager() #custom article manager

    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
        ordering=["-created",]
    def __str__(self):
        return self.title
    def total_love(self):
        return self.love.count()

    
    def secrete():
        print(secrete.tokens_urlsafe)
    
    def get_absolute_url(self): 
        # Note that when using reverse url, use the url name given to the view. The  name to 
        # access and the dic variable keyword must match the url variable in the url link
        # it must also have the inbuilt argument named 'kwargs'
        return reverse_lazy('blog:article_details', args=[self.slug])
        # kwargs={'slug': self.slug}
        # Alternatively, you can as well return the link directly by passing the base 
        # link and the field name to access
                         #return f'/blog/{self.title}'
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.header_image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_sze)
    #         img.save(self.header_image.path)

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
        # models.DateTimeField(default=now_plus_30)
        return datetime.now() + timedelta(days = 30) 
    
    def get_parent(self):
        if not self.parent :
            return True
        return False
    
    def get_children(self):
        return Comment.objects.filter(parent=self).reverse()
        # if Comment.objects.filter(parent=self.parent):
        #     return Comment.objects.filter(parent=self.parent)
       
       
    def total_love(self):
        return self.love.count()
    def __str__(self):
        return str(self.user)  +' __'  + str(self.article)


        # .filter((Q(for_field__is_null=True) | Q(for_field__bool=True))
# use the line of  code above to check for field with the field name first and the filter attribute second for multiple filtering of a foreign key


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    is_subscriber=models.BooleanField(default=False)

    verbose_name = 'subscriber'
    verbose_name_plural='subscribers'

    def __str__(self):
        return self.email


# class Advert(models.Model):
#     title        = models.CharField(max_length=100, blank=True, null=True)
#     amount =models.PositiveIntegerField(default=0)
#     content      = models.TextField(blank=True, null=True)
    
#     def __str__(sefl):
#         return self.title