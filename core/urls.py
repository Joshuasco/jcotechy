from django.urls import path
from . import views

app_name = "core"

urlpatterns=[
path('', views.HomeView.as_view(), name='home'),
path('projects/', views.ProjectView.as_view(), name='project'),
path('services/<pk>/', views.ServiceView.as_view(), name='service'),
path('opportunities/', views.OpportunityView.as_view(), name='opportunity'),
path('get_quote/', views.quote, name='quote'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('events/', views.event, name='event'),
path('subscribe/', views.subscribe, name='subscribe'),
]