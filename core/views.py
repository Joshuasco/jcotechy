from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView, View
from .models import (Review, Faq, Service, PortfolioCat, Portfolio, Position, 
Opportunity, Gallary, Event, EventCat, Contact, Quote,Subscriber, PrivacyPolicy )
from .forms import (OpportunityForm,)
from blog.models import Article
from .services import Services
from django.contrib import messages
from django.core.files import File
from django.conf import settings as _S


# Create your views here.

def search(request):
    if request.method == "GET":
        search_term = request.GET.get('search_term')
        path = request.GET.get('next')
        print(f"####################request receive##{path}################## {search_term}")
        try:
            if 'page' in search_term:
                if 'home' in search_term:
                    return redirect('core:home')
                elif 'about' in search_term:
                    return redirect('core:about')
                elif 'contact' in search_term:
                    print("contact page called--------------")
                    return redirect("core:contact")
                elif 'product' in search_term:
                    return redirect("core:product")
                elif 'project' in search_term or 'portfolio' in search_term:
                    return redirect('core:portfolio')
                elif 'blog' in search_term:
                    return redirect('blog:articles')
                elif 'signin' in search_term or 'login' in search_term:
                    return redirect('account:signin')
                elif 'signup' in search_term or 'register' in search_term:
                    return redirect('account:signup')
                else:
                    print(f"######## {search_term.index('page')} ############")
                    index = search_term.index('page')
                    print(index)
                    search_term=search_term[:index]
                    print(f"#################{search_term}################")
                    messages.warning(request, f"page with the name '{search_term}' does not exists")
                    
                    return redirect('core:home')
                
            else:
                # search_article=Article.articles.filter(title__in=search_term)
                return redirect(reverse('blog:articles')+f"?search_term={search_term}")
        except:
            print(f"#################{search_term}################")
            index = search_term.index('page')
            print(index)
            search_term=search_term[:index]
            print(f"#################{search_term}################")
            messages.warning(request, f"page with the name '{search_term}' does not exists")
            return redirect(reverse(path))
    
   

class HomeView(ListView):
    model=Service
    template_name='core/home.html'
    context_object_name = 'services'
    queryset= Service.services.all()

    
    """
    AUTOMATE SERVICES CREATION ON CALL TO HOME PAGE. 
    SHOULD EXECUTE ONCE

    """
    if _S.DEBUG:
        for service in Services:

            obj, created = Service.objects.get_or_create(title=service['title'],
                        short_description=service['short_dscript'],content=service['content'], published=service['published'])
            
            if created:
                # with open('{}'.format(service["svg_img"]), 'rb') as get_svg:
                print("######################################")
                print('{} service created'.format(service['title']))
                print("######################################")

            else:
                print("######################################")
                print('{} service already exist'.format(service['title']))
                print("######################################")
                

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context['reviews']=Review.reviews.all()
        context['faqs']=Faq.faqs.all()
        context['articles']=Article.articles.all()[:3]
        context['portfolios']=Portfolio.portfolios.all()[:2]

        return context



class ProjectList(ListView):
    model=Portfolio
    template_name='core/project.html'
    context_object_name = 'projects'
    # queryset= Service.services.all()

    def get_context_data(self):
        context = super(ProjectList, self).get_context_data()
        context['portfolios']=Portfolio.portfolios.all()
        context['portfolio_cats']=PortfolioCat.portfolio_cats.all()
        return context

    def get(self, request):
        if 'category' in self.request.get_full_path():
            slug_cat= request.GET.get('category')
            self.queryset= Portfolio.portfolios.filter(category=get_object_or_404(PortfolioCat, slug=slug_cat))
        return super(ProjectList, self).get(request)


class ProjectDetails(DetailView):
    model=Portfolio
    template_name='core/project_details.html'
    context_object_name = 'project'
   
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetails, self).get_context_data( *args, **kwargs)
        context['portfolios']=Portfolio.portfolios.all()
        context['portfolio_cats']=PortfolioCat.portfolio_cats.all()
        return context


class EventList(ListView):
    model=Event
    template_name='core/event.html'
    context_object_name = 'events'
    queryset= Event.events.all()

    def get_context_data(self):
        context = super(EventList, self).get_context_data()
        context['event_cats']=EventCat.event_cats.all()
        return context
    
    def get(self, request):
        if 'category' in self.request.get_full_path():
            slug_cat= request.GET.get('category')
            self.queryset= Event.events.filter(category=get_object_or_404(EventCat, slug=slug_cat))
        return super(EventList, self).get(request)


class EventDetails(DetailView):
    model=Event
    template_name='core/event_details.html'
    context_object_name = 'event'
    # queryset= Service.services.all()

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetails, self).get_context_data( *args, **kwargs)
        context['events']=Event.events.all()
        context['event_cats']=EventCat.event_cats.all()
        return context




class ServiceView(DetailView):
    model=Service
    template_name='core/service.html'
    context_object_name = 'service'
    # queryset= Service.services.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceView, self).get_context_data( *args, **kwargs)
        return context



def opportunity(request):
    # form_class=OpportunityForm
    template_name='core/opportunity.html'

    form = OpportunityForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid(self, form):
            form.save(commit=False)
            form.user=reques.user
            form.save()
            
    context={
        'opportunities':Opportunity.opportunities.all(),
        'form':form,
    }
    return render(request, template_name, context)

    

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
            messages.success(request, 'Thank you for contacting JCOTeck, we will respond to you shortly through your email ')
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




def subscribe(request):
    if request.method == "POST":
        email=request.POST.get('email')
        path=request.POST.get('next')
        if not '@' in email :
            return message.warning(request, 'please enter a vailid email')
        if Subscriber.objects.filter(email=email, is_subscriber=True).exists():
            messages.success(request, f"{email} is already a subsciber")
        else:
            Subscriber.objects.create(email=email,is_subscriber=True)
            messages.success(request, "you have successfully subscribe to Jcoteck email list, You can now receive updates and news from us")
        return redirect(path)

def unsubscribe(request):
    if request.method == "POST":
        email=request.POST.get('email')
        path=request.POST.get('next')
        if not '@' in email :
            return message.warning(request, 'please enter a vailid email')
        if not Subscriber.objects.filter(email=email, is_subscriber=True).exists():
            messages.success(request, f"{email} is not a subsciber")
        else:
            Subscriber.objects.create(email=email,is_subscriber=True)
            messages.success(request, "you have successfully unsubscribe to Jcoteck email list, You will no more receive updates and news from us")
        return redirect(path)



def privacyPolicy(request):
    context={
        'p_ps': PrivacyPolicy.p_ps.all()
     }
    return render(request, 'core/privacy_policy.html', context)