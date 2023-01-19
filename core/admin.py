from django.contrib import admin
from .models import (
    Review, Faq, Service, Portfolio, Gallary, Event, Quote, Contact, Opportunity, 
    Position, Quote, Product,
)
from django.utils.html import mark_safe, format_html
# Register your models here.

admin.site.register(Review)
admin.site.register(Faq)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','keywords','short_description','scheduled_on','created_on']
    list_editable=['keywords','short_description','scheduled_on']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','subject','created_on']

@admin.register(Product)
class ProduectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['user','position','content','published','is_applicant'] 

admin.site.register(Position)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','service','upload_file','created_on'] 

admin.site.register(Portfolio)


@admin.register(Gallary)
class GallaryAdmin(admin.ModelAdmin):
    list_display=['id','user_img','image_file','alt_text','img_url']
    list_display_links=['image_file',]
    readonly_fields=['img_url']
    search_fields=['alt_text','id',]
    search_help_text='search  using either field id or alt_text'
    
    def user_img(self, obj):
        return format_html(mark_safe('<a href="/admin/auth/user/?id={id}"><div style="text-align:center"><img  src="{url}" style="border-radius:50%" width="{width}" height={height} /><br>{username}</div></a>'.format(
            id=obj.user.id,
            url = obj.user.profile.image.url,
            width='50',height='50', 
            username=obj.user.username,
            )
        ))
    
    def image_file(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width='70',height='70',
            # width=obj.header_image.width,
            # height=obj.header_image.height,
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