from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import (Review, Faq, Service, Portfolio, Position, Opportunity, Gallary, Event, Contact, Quote)
from blog.models import Article
from .services import Services
from django.contrib import messages
from django.core.files import File

# Create your views here.
class HomeView(ListView):
    model=Service
    template_name='core/home.html'
    context_object_name = 'services'
    queryset= Service.services.all()

    
    """
    AUTOMATE SERVICES CREATION ON CALL TO HOME PAGE. 
    SHOULD EXECUTE ONCE

    """
    
    # for service in Services:

    #     obj, created = Service.objects.get_or_create(title=service['title'],
    #                 short_description=service['short_dscript'],content=service['content'], published=service['published'])
        
    #     if created:
    #         # with open('{}'.format(service["svg_img"]), 'rb') as get_svg:
    #         print("######################################")
    #         print('{} service created'.format(service['title']))
    #         print("######################################")

    #     else:
    #         print("######################################")
    #         print('{} service already exist'.format(service['title']))
    #         print("######################################")
            

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context['reviews']=Review.reviews.all()
        context['faqs']=Faq.faqs.all()
        context['articles']=Article.articles.all()
        context['portfolios']=Portfolio.portfolios.all()

        return context

class ProjectView(ListView):
    model=Service
    template_name='core/project.html'
    context_object_name = 'projects'
    # queryset= Service.services.all()

    def get_context_data(self):
        context = super(ProjectView, self).get_context_data()
        context['reviews']=Review.reviews.all()
        context['faqs']=Faq.faqs.all()
        context['articles']=Article.articles.all()
        context['portfolios']=Portfolio.portfolios.all()
        return context

class ServiceView(DetailView):
    model=Service
    template_name='core/service.html'
    context_object_name = 'service'
    # queryset= Service.services.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceView, self).get_context_data( *args, **kwargs)
        context['reviews']=Review.reviews.all()
        context['faqs']=Faq.faqs.all()
        context['articles']=Article.articles.all()
        context['portfolios']=Portfolio.portfolios.all()
        return context

class OpportunityView(ListView):
    model=Opportunity
    template_name='core/opportunity.html'
    context_object_name = 'opportunities'
    queryset= Opportunity.opportunities.all()

    

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    first_name=request.POST.get('first_name', None)
    last_name=request.POST.get('last_name', None)
    email=request.POST.get('email', None)
    subject=request.POST.get('subject', None)
    message=request.POST.get('message', None)

    print(f'{first_name}--1 {last_name}--2 {email}--3 {subject}--4 {message}--5')
    if request.method == 'POST':
        if first_name !=None and last_name !=None and email !=None and subject !=None and message !=None:
            Contact.objects.create(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
            messages.success(request, 'Thank you for contacting jcotech, we will respond to you shortly through your email ')
        else:
            messages.error(request, 'plesase fill all fields')
    return render(request, 'core/contact.html')

def quote(request):
    full_name=request.POST.get('full_name', None)
    email=request.POST.get('email', None)
    service=request.POST.get('service', None)
    upload_file=request.POST.get('file', None)
    message=request.POST.get('message', None)

    print(f'{full_name}--1 {email}--2 {service}--3 {upload_file}--4 {message}--5')
    if request.method == 'POST':
        if full_name !=None and email !=None and service !=None and message !=None:
            Quote.objects.create(full_name=full_name, email=email, service=service, upload_file=upload_file, message=message)
            messages.success(request, 'Thank you for contacting jcotech, we will respond to you shortly through your email ')
        else:
            messages.error(request, 'plesase fill all fields')

    print(f"-----------path = --------------{request.GET.get('path', None)}--------------")
    return redirect(request.POST.get('path'))

def event(request):
    context={
        'events':Event.events.all()
    }
    return render(request, 'core/event.html', context)