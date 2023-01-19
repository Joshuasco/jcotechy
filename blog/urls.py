from django.urls import path
from . import views

app_name = "blog"

urlpatterns=[
path('', views.article, name='articles' ),
path('<slug:slug>/', views.articleDetails, name='article_details' ),
path('<slug:slug>/love/', views.loveArticle, name='love_article' ),
path('<slug:slug>/comment/', views.comment, name='comment' ),
path('<slug:slug>/comment/love/<int:id>/', views.loveComment, name='love_comment' ),
path('<slug:slug>/comment/edit/<int:id>/', views.editComment, name='edit_comment' ),
path('<slug:slug>/comment/delete/<int:id>/', views.deleteComment, name='delete_comment' ),
]