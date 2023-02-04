from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django.utils.html import mark_safe, format_html

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     model=Profile
#     fields=['user_img','image']

    

class ProfileInline(admin.StackedInline):
    model=Profile
    

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','user','user_password','first_name', 'last_name','is_staff','is_superuser','last_login','date_joined']
    list_display_links=['user',]
    # fields=['user_img','username','password','first_name', 'last_name','last_login','date_joined']
    # fields += ['user_img']
    # list_filter=['id','username',]
    readonly_fields=['user_img','username','password','last_login','date_joined']
    search_fields=['username','id','first_name', 'last_name','is_staff','is_superuser']
    inlines=[ProfileInline]

    def get_list_filter(self, request):
        """
        Return a sequence containing the fields to be displayed as filters in
        the right sidebar of the changelist page.
        """
        if not request.user.is_superuser:
            return super(UserAdmin, self).get_list_filter(request)
        return self.list_filter

    def get_fields(self, request, obj):
        
        fd=super(UserAdmin, self).get_fields(request,obj)
        
        if not request.user.is_superuser:
            fields=['user_img','username','password','first_name', 'last_name','last_login','date_joined']
            return fields
        return fd
    def get_queryset(self, request, *args, **kwargs):
        qs = super(UserAdmin, self).get_queryset(request, *args, **kwargs)
        # qs=qs.annotate(_user_imge=format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
        #     url = self.profile.image.url,
        #     width='70',height='70',
           
        #     ))))
        if request.user.is_superuser:
                return qs
        return qs.filter(username=request.user.username)

    def user_img(self, obj):
        return format_html( mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.profile.image.url,
            width='70',height='70',
           
            )))


    def user(self, obj):
        return mark_safe('<div style="text-align:center"><img  src="{url}" style="border-radius:50%" width="{width}" height={height} /><br>{username}</div>'.format(
            url = obj.profile.image.url,
            width='50',height='50', 
            username=obj.username,
            )
        )
    def user_password(self, obj):
        return obj.password[:10]+'...'
