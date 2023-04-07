from django.contrib import admin
from .models import (
    Review, Faq, Service, PortfolioCat, Portfolio, Gallary, EventCat, Event,
     Quote, Contact, Opportunity,Subscriber, Position, Quote, PrivacyPolicy
)
from django.utils.html import mark_safe, format_html
# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user_img','published', 'created_on','updated_on']
    list_filter = ['published','created_on']
    readonly_fields=['created_on','updated_on']
    
    def user_img(self, obj):
        return format_html(mark_safe('<a href="/admin/auth/user/?id={id}"><div style="text-align:center"><img  src="{url}" style="border-radius:50%" width="{width}" height={height} /><br>{username}</div></a>'.format(
            id=obj.user.id,
            url = obj.user.profile.image.url,
            width='50',height='50', 
            username=obj.user.username,
            )
        ))



@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question','published', 'created_on','updated_on']
    list_filter = ['published','created_on'] 
    readonly_fields=['created_on','updated_on'] 



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email','is_subscriber','verified_email','subscribed_on'] 
    list_filter = ['is_subscriber','subscribed_on']
    readonly_fields=['subscribed_on']  



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'published','created_on']
    list_filter = ['published','created_on'] 
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields=['created_on','updated_on']



@admin.register(EventCat)
class EventCatAdmin(admin.ModelAdmin):
    list_display=['title','img','published','created_on','updated_on']
    list_editable=['published']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields=['created_on','updated_on']
    search_fields=['title','created_on']
    search_help_text=['search using the field email created_on or updated_on']

    def img(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width='50',height='50',
            )
            )
        )



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','img','category','scheduled_on','published','created_on']
    list_editable=['published','scheduled_on']
    list_filter = ['published','created_on'] 
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields=['created_on','updated_on']

    def img(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width='50',height='50',
            )
            )
        )



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','subject','created_on']
    search_fields=['email','created_on']
    search_help_text=['search using the field email or created_on']
    readonly_fields=['created_on','updated_on']



@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['user','full_name','position','published','is_applicant','created_on'] 
    readonly_fields=['created_on','updated_on']

admin.site.register(Position)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','service','upload_file','created_on'] 



@admin.register(PortfolioCat)
class PortfolioCatAdmin(admin.ModelAdmin):
    list_display=['title','img','published','created_on','updated_on']
    list_editable=['published']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields=['created_on','updated_on']
    search_fields=['title','created_on']
    search_help_text=['search using the field email created_on or updated_on']

    def img(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width='50',height='50',
            )
            )
        )




@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=['title','img','category','review','published','created_on','updated_on']
    list_filter=['published','created_on']
    list_editable=['published']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields=['created_on','updated_on']
    search_fields=['title']
    search_help_text=['search  using the field title']

    def img(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width='50',height='50',
            )
            )
        )



@admin.register(Gallary)
class GallaryAdmin(admin.ModelAdmin):
    list_display=['id','user_img','img_file','img_url']
    list_display_links=['img_file',]
    list_filter = ['created_on']
    readonly_fields=['created_on','updated_on','img_url']
    search_fields=['caption','id',]
    search_help_text=['search  using either field id or caption']
    
    def user_img(self, obj):
        return format_html(mark_safe('<a href="/admin/auth/user/?id={id}"><div style="text-align:center"><img  src="{url}" style="border-radius:50%" width="{width}" height={height} /><br>{username}</div></a>'.format(
            id=obj.user.id,
            url = obj.user.profile.image.url,
            width='50',height='50', 
            username=obj.user.username,
            )
        ))
    
    def img_file(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} /><br>{caption}'.format(
            url = obj.image.url,
            width='50',height='50',
            caption=obj.caption
            )
    ))

    def img_url(self,obj):
        btn_id='copy-'+str(obj.id)
        return format_html(
            mark_safe(
                f"""<input  text="text" id="{btn_id}" value="{obj.image.url}" readonly><a href="#" 
                onclick="document.querySelector(\'#{btn_id}\').select(); document.execCommand(\'copy\'); window.alert('url copied successfully');"
                 class="addlink">copy url</a>"""
            )
        )



@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display=['title','img','published','created_on','updated_on']
    list_editable=['published']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields=['created_on','updated_on']
    
    def img(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width='50',height='50',
            )
            )
        )
