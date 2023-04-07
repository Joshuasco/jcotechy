# from email import message
# from email.policy import default
# from operator import add
# from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.sites.shortcuts import get_current_site
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import redirect, render, get_object_or_404
# from django.urls import reverse
# from django.contrib import messages
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes, force_str
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# from .forms import RegistrationForm
# from checkout.models import Order
# from .models import Customer,   Address
# from .forms import UserEditForm, AddressForm
# from .tokens import account_activation_token


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, AccountUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout






#begin signup
from django.http import HttpResponse  
from django.shortcuts import render, redirect 
from django.urls import reverse, reverse_lazy 
from django.contrib.auth import login, authenticate  
from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.conf import settings


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import sendgrid
from sendgrid.helpers.mail import *

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# message = Mail(
#     from_email='from_email@example.com',
#     to_emails='to@example.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

def send_email(to_email, subject, body):
    print(f"############## {settings.DEFAULT_FROM_EMAIL} ##############")
    message = Mail(
        from_email="info@jcoteck.com",
        to_emails=['emekaodigbo1@gmail.com', 'joshuaodigbo1@gmail.com'],
        subject=subject,
        # html_content=body
        # subject = "Subject line for the email"
        html_content = body
        )
        
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print("############## RESPONSE STATUS CODE  ###################")
        print(response.status_code)
        print("############## RESPONSE BODY  ###################")
        print(response.body)
        print("############## RESPONSE HEADER  ###################")
        print(response.headers)
    except Exception as e:
        print("############## ERROR ENCOUNTERED  ###################")
        print(e)




# def signup(request):  
#     if request.method == 'POST':  
#         form = SignupForm(request.POST)  
#         if form.is_valid():  
#             # save form in the memory not in database  
#             user = form.save(commit=False)  
#             user.is_active = False  
#             user.save()  
#             # to get the domain of the current site  
#             current_site = get_current_site(request)  
#             mail_subject = 'Activation link has been sent to your email id'  
#             message = render_to_string('acc_active_email.html', {  
#                 'user': user,  
#                 'domain': current_site.domain,  
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
#                 'token':account_activation_token.make_token(user),  
#             })  

#             to_email = form.cleaned_data.get('email')  
#             email = EmailMessage(  
#                         mail_subject, message, to=[to_email]  
#             )  
#             email.send()  
#             messages.info(request, "Please confirm your email address to complete the registration")
#             return redirect('account:signup')
#     else:  
#         form = SignupForm()  
#     return render(request, 'account/signup.html', {'form': form}) 


#end signup


#activate
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        messages.success(request, 'Thank you for your email confirmation. You can now login to your account.' )
        return redirect('account:signin')  
    else:  
        messages.success(request, 'Activation link is invalid!' )
        return redirect('account:signin')    
#end activate


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             # should verify email before login
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'account/signup.html', {'form': form})




 






















def signin(request):
    path= request.POST.get('next')
    email_username=request.POST.get('email_or_username', None)
    password=request.POST.get('password', None)
    if request.method == "POST":
        if email_username is None or password is None:
            messages.info(request,"one or more fields are empty")
            return redirect('account:signin')
        if  '@' in email_username:
            if not User.objects.filter(email=email_username ).exists():
                messages.error(request,"email doesn't exists, signup with this email")
                return redirect('account:signin')
            username=User.objects.filter(email=email_username)[0].username
            authenticate_user=auth.authenticate(username=username, password=password)
            
            if authenticate_user:
                auth.login(request, authenticate_user)
                messages.success(request,f"{email_username} signin successfully")
                return redirect('core:home')
            else:
                messages.error(request,"wrong credentials")
                return redirect('account:signin')
        else:
            authenticate_user=auth.authenticate(username=email_username, password=password)
            if authenticate_user:
                auth.login(request, authenticate_user)
                messages.success(request,f"{email_username} signin successfully")
                if path:
                  return redirect(path)  
                return redirect("core:home")
            else:
                messages.error(request,"wrong credentials")
                return redirect('account:signin')
    from django.core.mail import send_mail
    message = Mail(
        from_email='info@jcoteck.com',
        to_emails=["emekaodigbo1@gmail.com",],
        subject="u are welcomw to jcoteck",
        # html_content=body
        # subject = "Subject line for the email"
        html_content = "my html content goes here"
        # Content("text/plain", "Body of the email")
        )
        
    try:
        # sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        print("done")


        subject = 'Test Email'
        message = 'This is a test email message'
        email_from = 'emekaodigbo1@gmail.com'
        recipient_list = ['joshuaodigbo1@gmail.com', 'jcoteck@gmail.com']
        
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        send_mail(
            "u are welcomw to jcoteck",
            # html_content=body
            # subject = "Subject line for the email"
        "my html content goes here"
            'emekaodigbo1@gmail.com',
            ["joshuaodigbo1@gmail.com",],
            fail_silently=False,
        )
        messages.info(request, "message sent")
        # response = sg.send(message)
        # print("############## RESPONSE STATUS CODE  ###################")
        # print(response.status_code)
        # print("############## RESPONSE BODY  ###################")
        # print(response.body)
        # print("############## RESPONSE HEADER  ###################")
        # print(response.headers)
    except Exception as e:
        print("############## ERROR ENCOUNTERED  ###################")
        print(e)
            
    return render(request, 'account/signin.html')

def signup(request):
    username=request.POST.get('username', None)
    email=request.POST.get('email', None)
    password_1=request.POST.get('password', None)
    password_2=request.POST.get('confirm_password', None)
    context={
        'username':username,
        'email' :email,
        'password_1':password_1,
        'password_2':password_2,
    }
    send_email('emekodigbo1@gmail.com', "Integrating sendgird mail", "testing out sendgrid mail integrations")
    print("######################## MESSAGE SENT ################")
    if request.method == 'POST':
        if username !=None and email !=None and password_1 !=None and password_2 !=None:
            
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'username already exist, please use another username')
                return redirect('account:signup')
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'email already exist, please use another email')
                return redirect('account:signup')
            if password_1 != password_2:
                messages.warning(request, 'passwords do not match, ensure to enter the correct password')
                return redirect('account:signup')
            current_user=User.objects.create_user(username=username, email=email, password=password_1, is_active=False)
            
            # User.objects.create_user(username=username, email=email, password=password_1)
            
            #verify email address
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id' 
            uid=urlsafe_base64_encode(force_bytes(current_user.pk)),  
            token=account_activation_token.make_token(current_user),  
            message = render_to_string('account/verify_account.html', {  
                'user': current_user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(current_user.pk)),  
                'token':account_activation_token.make_token(current_user),  
                'verification_url' : request.build_absolute_uri(reverse('account:activate', kwargs={'uidb64': uid, 'token': token}))
            })  
            to_email = email 
            # email = EmailMessage(  
            #             mail_subject, message, to=[to_email]  
            # )  
            # email.send() 

            send_email(to_email, mail_subject, message)
            print("######################## MESSAGE SENT ################")

            messages.info(request, "Please confirm your email address to complete the registration")
            return redirect('account:signup')

            # messages.success(request, 'signup successfull, click the signin button to signin')
            # return redirect('account:signup')
        else:

            messages.warning(request, 'one or more filed(s) is(are) empty please fill all filleds')
            return redirect('account:signup')
    return render(request, 'account/signup.html', context)
 
@login_required
def signout(request):
    path=request.GET.get('next')
    logout(request)
    messages.success(request, 'singnout successful')
    if path:
        return redirect(path)  
    return redirect("core:home")

@login_required
def profile(request):
    if request.method == 'POST':
        a_form = AccountUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if a_form.is_valid() and p_form.is_valid():
            a_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
 
    else:
        a_form = AccountUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
 
    context = {
        'a_form': a_form,
        'p_form': p_form
    }
 
    return render(request, 'account/profile.html', context)











