from django.urls import path
from . import views

app_name = "core"

urlpatterns=[
path('', views.HomeView.as_view(), name='home'),
path('projects/', views.ProjectList.as_view(), name='project'),
path('projects/<slug>', views.ProjectDetails.as_view(), name='project_details'),
path('events/', views.EventList.as_view(), name='event'),
path('events/<slug>', views.EventDetails.as_view(), name='event_details'),
path('services/<pk>/', views.ServiceView.as_view(), name='service'),
path('opportunities/', views.opportunity, name='opportunity'),
path('get_quote/', views.quote, name='quote'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('subscribe/', views.subscribe, name='subscribe'),
path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
path('search', views.search, name='search' ),
path('privacy_policy/', views.privacyPolicy, name='privacy_policy'),
]