from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import (Article, Comment, Category, Tag, Share, Viewer)
from .forms import CommentForm
from account.models import Profile
from datetime import timedelta, datetime
from django.utils import timezone
from django.db.models import Count, Q
from django.contrib.sites.shortcuts import get_current_site  
import os
from io import BytesIO
import io
from gtts import gTTS  
# import pyttsx3         
import math
from django.utils.html import strip_tags                                                                                      
# Create your views here.
 

def searchArticle(request):   
    # Calculate the date one week ago
    one_week_ago = datetime.now() - timedelta(weeks=1)

    # Query the database to get the most popular posts from the past week
    popular_posts = Post.objects.filter(date_published__gte=one_week_ago).annotate(num_likes=Count('likes')).order_by('-num_likes')

    # Loop through the queryset to display the popular posts
    for post in popular_posts:
        print(post.title)
    

    # Get current date
    today = datetime.date.today()

    # Calculate date 7 days ago
    date_7_days_ago = today - timedelta(days=7)
    

    # Filter posts created within the last 7 days
    recent_posts = Article.articles.filter(created__date=date_7_days_ago)

    #a week
    one_week_ago = timezone.now() - timezone.timedelta(weeks=1)
    posts = Post.objects.filter(date_posted__gte=one_week_ago)
    return render(request, 'blog/articles.html', recent_posts)


# estimated read time at 275 wpm
def get_read_time(html_content):
    # Remove HTML tags from the content
    text = strip_tags(html_content)

    # Count the number of words
    word_count = len(text.split())

    # Calculate the estimated read time (assuming an average reading speed of 275 words per minute)
    read_time_minutes = math.ceil(word_count / 275)
    return read_time_minutes

# get audio from article
def get_audio(title, html_content):
    
    text = strip_tags(html_content)
    text = title + ". " +text

    path=f'static/myaudio/{title.replace(" ", "_")}.mp3'
    tts = gTTS(text, lang='en', slow=False)
    tts.save(path)

    
    # Create an in-memory file object
        # audio_file = io.BytesIO()
    # Save the audio to the file object
        # tts.write_to_fp(audio_file)
    # Seek to the beginning of the file object
        # audio_file.seek(0)
    # Return the file object
    return path



# def get_audio_1(title, html_content):
#     text =strip_tags(title) + '. ' + strip_tags(html_content)
#     # initialize Text-to-speech engine  
#     engine = pyttsx3.init()  
#     # convert this text to speech  
#     path=f'static/myaudio/{title.replace(" ", "_")}.mp3'
#     engine.save_to_file(text, path )
#     # engine.say(text)  
#     engine.setProperty('rate', 275)  # set the speaking rate
#     engine.setProperty('voice', 'en-us')  # set the language of the audio
#     return engine


def playAudio(request, slug):
    article=get_object_or_404(Article, slug=slug)
    title= article.title
    content=article.content

    data={}
    path= f'static/myaudio/{title.replace(" ", "_")}.mp3'
    try:
        # with open(path, 'rb') as audio_file:
        #     if audio_file:
                #  print("audio file exists+++++++++++++")

        audio=get_audio(title, content)
        print("audio file processing....")

       
    except:
        print("please check your internet connection ")
        # print("audio file does mot exists+++++++++++++ creating one")
        

        # audio.runAndWait() 
        # audio.stop() 
   
    data['path']=path
    return JsonResponse(data)

def article(request):

    today= datetime.now()
    a_month_ago= today - timedelta(days=30)

    recent_articles=Article.articles.all()
    trending_articles=Article.articles.filter(created__gte=a_month_ago,created__lte=today).annotate(num_count=((Count('love')+Count('comment'))/2)).order_by('-num_count')
    reviewed_articles= Article.articles.filter(is_reviewed=True)

    articles = ''
    if 'category' in request.GET:
        category_slug=request.GET.get('category')
        articles=Article.articles.filter(category__in=Category.objects.filter(slug=category_slug))
    
    if 'tag' in request.GET:
        tag_slug=request.GET.get('tag')

    if 'reviewed_articles' in request.GET:
        articles=reviewed_articles

    if 'trending_articles' in request.GET:
        articles=trending_articles
    
    if 'recent_articles' in request.GET:
        articles=recent_articles

    if 'search_term' in request.GET:
        search_term = request.GET.get("search_term")
        articles= Article.articles.filter(title__icontains=search_term) 
        
    context={
    'trending_articles':trending_articles,
    'reviewed_articles':reviewed_articles,
    'recent_articles': recent_articles,
    'articles': articles,
    'categories': Category.categories.all(),
    'featured_articles':Article.articles.filter(is_featured=True),
        }
    
    return render(request, 'blog/articles.html', context)


def articleDetails(request, slug):

    today= datetime.now()
    a_week_ago= today + timedelta(weeks=-1)

    trending_articles=Article.articles.filter(created__lte=a_week_ago).annotate(num_love=((Count('love')+Count('comment'))/2)).order_by('-num_love')
    recent_articles=Article.articles.all()
    reviewed_articles= Article.articles.filter(is_reviewed=True)
    articles =Article.articles.all()
    article= get_object_or_404(Article,is_published=True, slug=slug )
    read_time= get_read_time(article.content)
    categories= Category.objects.all()
    viewer(request, slug) 

    print((f'############## {article.header_image.url} ###################'))
    print((f'############## {request.build_absolute_uri} ###################'))
    print((f'############## {get_current_site(request)} ###################'))

    context={
    'articles':articles, 
    'article': article,
    'id':       article.id,
    'read_time':read_time,
    'audio': f'/static/myaudio/{article.title.replace(" ", "_")}.mp3',
    'domain': get_current_site(request) , 
    'recent_articles': recent_articles,
    'related_articles':Article.articles.filter(category=article.category),
    'trending_articles':trending_articles,
    'reviewed_articles':reviewed_articles,
    'comment_form':CommentForm(),
    'categories':categories,
        }

    return render(request, 'blog/article_details.html', context)

    

@login_required
def loveArticle(request, slug):
    article=get_object_or_404(Article, slug=slug)
    profile = get_object_or_404(Profile, user=request.user)
    if article.love.filter(id=profile.id).exists():
        article.love.remove(profile)
        article.save()
        return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
    article.love.add(profile)
    article.save()
    return redirect(reverse('blog:article_details', kwargs={'slug':slug}))

@login_required
def comment(request, slug):
    commentForm= CommentForm()
    if request.method=="POST":
        commentForm=CommentForm(request.POST or None)
        if commentForm.is_valid():
            c_f = commentForm.save(commit=False)
            c_f.user=request.user
            try:
                if 'comment_id' in request.get_full_path():
                    parent_id=request.POST.get('comment_id')
                    parent_id=str(request.get_full_path()).split('=')[1]
                if parent_id is not None:
                    parent=get_object_or_404(Comment, id=parent_id)
                    c_f.parent=parent
                c_f.article=get_object_or_404(Article, slug=slug)
                c_f.save()
                return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
            except:
                c_f.article=get_object_or_404(Article, slug=slug)
                c_f.save()
                return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
    context={
        'comment_form':commentForm
    }
    return reverse_lazy('blog:article_details', kwargs={'slug':slug})

@login_required
def loveComment(request, slug, id):
    comment=get_object_or_404(Comment, id=id)
    if comment.love.filter(id=request.user.id).exists():
        comment.love.remove(request.user)
        comment.save()
        return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
    comment.love.add(request.user)
    comment.save()
    return redirect(reverse('blog:article_details', kwargs={'slug':slug}))

@login_required
def editComment(request, slug, id):
    comment=get_object_or_404(Comment, id=id, user=request.user)
    comment_form=CommentForm(instance=comment)
    if request.method == 'POST':
        comment_form=CommentForm(instance=comment, data=request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
    context={
    'article': get_object_or_404(Article,is_published=True, slug=slug ),
     'comment_form':comment_form,
     'comment_id':id,
        }
    return render(request, 'blog/article_details.html', context)


@login_required
def deleteComment(request, slug, id):
    comment=get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
   

@login_required
def love(request, id):
    comment=get_object_or_404(Comment, id=id)
    if comment.love.filter(user=request.user.profile_set).exists():
        comment.love.remove(request.user.id)
    else:
        comment.love.add(request.user.id)

def share(request, slug, social_medium):
    article=get_object_or_404(Article, slug=slug)
    social_medium= social_medium.strip()
    print("################# CALLED 333333333333")
    if social_medium == "facebook":
        social_medium = "facebook"
    elif social_medium == "twitter":
        social_medium = "twitter"
    elif social_medium == "linkedin":
        social_medium = "linkedin"
    elif social_medium == "whatsapp":
        social_medium = "whatsapp"
    elif social_medium == "telegram":
        social_medium = "telegram"
    else:
        return redirect(reverse('blog:article_details', kwargs={'slug':slug}))

    share_obj=Share.objects.create(article=article, social_medium=social_medium )

    return redirect(reverse('blog:article_details', kwargs={'slug':slug}))



def viewer(request, slug):
    article= get_object_or_404(Article, slug=slug)
    ip=request.META.get('HTTP_X_FORWARDED_FOR')
    print(f"{ip}##############")
    if ip:
        
        ip.split(',')[0]
    else:
        ip=request.META.get('REMOTE_ADDR')
    Viewer.objects.create(article=article, ip=ip,)
    return 'ip added'