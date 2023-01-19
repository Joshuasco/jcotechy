from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import (Article, Comment, Category, Tag,)
from .forms import CommentForm
from account.models import Profile
import datetime
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count, Q


# Create your views here.

    
def searchArticle(request):

    # Import the required modules
    from django.db.models import Count
    from datetime import datetime, timedelta

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


def article(request):
    articles = Article.articles.all()
    if 'category' in request.GET:
        category_slug=request.GET.get('category')
        articles=Article.articles.filter(category__in=Category.objects.filter(slug=category_slug))
    
    if 'tag' in request.GET:
        tag_slug=request.GET.get('tag')
        articles=Article.articles.filter(tags__in=Tag.objects.filter(slug=tag_slug))

    today= datetime.datetime.now()
    a_week_ago= today + datetime.timedelta(weeks=-1)
    trending_articles=Article.articles.filter(created__lte=a_week_ago).annotate(num_love=((Count('love')+Count('comment'))/2)).order_by('-num_love')
    a_week_ago= today - datetime.timedelta(weeks=1)
    reviewed_articles= Article.articles.filter(updated__lte=a_week_ago)
   
    context={
    'trending_articles':trending_articles,
    'reviewed_articles':reviewed_articles,
    'articles': articles,
    'categories': Category.categories.all(),
    'featured_articles':Article.articles.filter(is_featured=True),
        }
    
    return render(request, 'blog/articles.html', context)


def articleDetails(request, slug):

    today= datetime.datetime.now()
    a_week_ago= today + datetime.timedelta(weeks=-1)
    trending_articles=Article.articles.filter(created__lte=a_week_ago).annotate(num_love=((Count('love')+Count('comment'))/2)).order_by('-num_love')
    reviewed_articles= Article.articles.filter(updated__lte=a_week_ago).order_by('-updated')
    articles =Article.articles.all()
    article= get_object_or_404(Article,is_published=True, slug=slug )
    categories= Category.objects.all()

    context={
    'articles':articles, 
    'article': article,
    'id':       article.id,
    'trending_articles':trending_articles,
    'reviewed_articles':reviewed_articles,
    'comment_form':CommentForm(),
    'categories':categories,
        }

    return render(request, 'blog/article_details.html', context)


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

def loveComment(request, slug, id):
    comment=get_object_or_404(Comment, id=id)
    if comment.love.filter(id=request.user.id).exists():
        comment.love.remove(request.user)
        comment.save()
        return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
    comment.love.add(request.user)
    comment.save()
    return redirect(reverse('blog:article_details', kwargs={'slug':slug}))

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



def deleteComment(request, slug, id):
    comment=get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect(reverse('blog:article_details', kwargs={'slug':slug}))
    # return reverse_lazy('blog:article_details', kwargs={'slug':slug})

def love(request, id):
    comment=get_object_or_404(Comment, id=id)
    if comment.love.filter(user=request.user.profile_set).exists():
        comment.love.remove(request.user.id)
    else:
        comment.love.add(request.user.id)


