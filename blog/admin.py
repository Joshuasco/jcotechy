from django.contrib import admin
from .models import Category, Tag, Article, Comment
from django.db.models import Count
from django.utils.html import format_html, mark_safe
from django.shortcuts import reverse

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,'title','header_img', 'author_by',  'category','all_tags','likes','comments','is_published', 'created', 'updated']
    list_display_links=['title',]
    list_filter = ['is_published','created']
    list_select_related = True
    readonly_fields=['author','header_img']
    list_editable = ['is_published', ]
    fields=[('is_published','is_featured','is_sponsored','is_project','is_product','is_event','is_video'),'header_img','author',\
    ('header_image','alt_text'),('title','slug'),'video','content',('category','tags')]
    prepopulated_fields = {'slug': ('title',)}
    list_per_page=3
    actions=['update_field',]
    date_hierarchy = 'created'
    search_help_text = 'search article by field id, title, or date_created'
    date_hierarchy = None
    save_as = True
    save_as_continue = False
    save_on_top = False
    # paginator = Paginator
    preserve_filters = False

    admin.site.site_header = "User Admin"
    admin.site.site_title = "JCOTECH Admin Portal"
    admin.site.index_title = "Welcome to JCOTECH Admin"

    actions = ('update post',)
    # action_form = helpers.ActionForm
    # actions_on_top = True
    # actions_on_bottom = False
    # actions_selection_counter = True
    # checks_class = ModelAdminChecks

    # def lookup_allowed(self, lookup, value):
    #     # Don't allow lookups involving passwords.
    #     return not lookup.startswith("password") and super().lookup_allowed(
    #         lookup, value
    #     )
    # list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("title__icontains", "id",'is_published','created',)
    # ordering = ("username",)
    filter_horizontal = (
        # "groups",
        # "user_permissions",
        "love",
        
    )

    # def get_list_filter(self, request):
    #     """
    #     Return a sequence containing the fields to be displayed as filters in
    #     the right sidebar of the changelist page.
    #     """
    #     lf=super(ArticleAdmin, self).get_list_filter(request)
    #     if not request.user.is_superuser:
    #         list_filter = ['is_published',]
    #         return list_filter
    #     return lf

    def get_fields(self, request, obj):
        
        fd=super(ArticleAdmin, self).get_fields(request,obj)
        
        if not request.user.is_superuser:
            fields=[('is_published','is_video'),'header_img',('header_image','alt_text'),('title','slug'),'video','content',('category','tags')]
            return fields
        return fd


    def header_img(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.header_image.url,
            width='70',height='70',
            # width=obj.header_image.width,
            # height=obj.header_image.height,
            )
    )

    def author_by(self, obj):
        return mark_safe('<a href="/admin/auth/user/?id={id}"><div style="text-align:center"><img  src="{url}" style="border-radius:50%" width="{width}" height={height} />{username}</div></a>'.format(
            id=obj.author.user.id,
            url = obj.author.image.url,
            width='50',height='50', 
            username=obj.author.user.username,
            )
        )
    def get_queryset(self, request, *args, **kwargs):
        qs = super(ArticleAdmin, self).get_queryset(request, *args, **kwargs)
        qs=qs.annotate(_comments=Count('comment', unique=True ), _likes=Count('love', unique=True),)
        if request.user.is_superuser:
                return qs
        return qs.filter(author=request.user.profile)
        # admin.site.register(Tour,TourAdmin)


    def all_tags(self, obj):
        display_text = ", ".join([
        "<a href={}>{}</a>".format(
        reverse('admin:{}_{}_change'.format(obj._meta.app_label, 'tag'),
        args=(tag.pk,)),
        tag.title)
        for tag in obj.tags.all()
        ])
        if display_text:
            return mark_safe(display_text)
        return '-'

    def likes(self, obj):
        return obj.total_love()

    # investigate on mark_safe, format_html and format differences
    def comments(self, obj):
        url = format_html(
                "<a style='padding:.5em;background-color:blue;border-radius:5px;color:white;' title='click to view' href=/admin/blog/comment/?article__id__exact={}>{}</a>".format(
    obj.id,str(obj._comments) )
            )
        if url:
            return url
        return '-'
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
        # Only set author during the first save.
            obj.author = request.user.profile
        return super().save_model(request, obj, form, change)

    # comments.admin_order_field = '_comments'
    # likes.admin_order_field = '_likes'
    
    #    def get_form(self, request, obj=None, *args, **kwargs):
    # def get_form(self, request, obj=None, *args, **kwargs):
    #     form = super(ArticleAdmin, self).get_form(request, obj=None,  *args, **kwargs)
    #     if request.user.is_superuser is False:
    #         # form.base_fields['department'].queryset = Department.objects.filter(
    #         #     name = request.user.customuser.department.name)
    #         form.author=request.user.profile
    #         return form

    


   
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields=[ 'is_published','user','article','content','created','updated' ]
    list_display = ['id','parent_id','articles','comment_by','comments',  'replies','likes', 'is_published','created','updated']
    list_display_links=['comments',]
    list_filter = ['is_published','created']
    readonly_fields=['user','created','updated',]
    list_editable = ['is_published',]
    search_fields=['id','created',]
    search_help_text="search comments using the field 'id','created' or 'parent_id' "
    

    def save_model(self, request, obj, form, change):
        if not obj.pk:
        # Only set author during the first save.
            obj.user = request.user
            super().save_model(request, obj, form, change)

    # def get_list_filter(self, request):
    #     lf= super(CommentAdmin, self).get_list_filter(request)
    #     if  request.user.is_superuser:
    #         list_filter=['is_published','created','article']
    #         return list_filter
    #     return lf

    def articles(self, obj):
        return mark_safe('<div><a href="/admin/blog/article/?id={id}"><img  src="{url}"  width="{width}" height={height} /><br>{username}</a></div>'.format(
            id=obj.article.id,
            url = obj.article.header_image.url,
            width='70',height='60', 
            username=obj.article.title,
            )
        )

    def comment_by(self, obj):
        return mark_safe('<div style="text-align:center"><img  src="{url}" style="border-radius:50%" width="{width}" height={height} />{username}</div>'.format(
            url = obj.user.profile.image.url,
            width='50',height='50', 
            username=obj.user.username,
            )
        )

    def get_queryset(self, request, *args, **kwargs):
        qs = super(CommentAdmin, self).get_queryset(request, *args, **kwargs)
        qs=qs.annotate(_likes=Count('love', unique=True),)
        if request.user.is_superuser:
            return qs
        return qs.filter(article__in=request.user.profile.article_set.all())

    def comments(self, obj):
        # if obj.get_parent():
            return obj.content
    
    def parent_id(self, obj):
        if not obj.get_parent():
            return obj.parent.id

    def replies(self, obj):
        return obj.get_children().count()

    def likes(self, obj):
        return obj._likes


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['slug','title']
    prepopulated_fields = {'slug': ('title',)}
    # fields=['slug','title','is_published']
    # readonly_fields =['slug','title','is_published',]

    # def get_readonly_fields(self, request, obj=None):
    #     rof = super(CategoryAdmin, self).get_readonly_fields(request, obj)
    #     if  not request.user.is_superuser:
    #         self.readonly_fields =('slug','title','is_published',)
    #         # return self.readonly_fields
    #         rof += ('slug','title','is_published','created',)
    #         return rof

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display= ['slug','title']
    prepopulated_fields = {'slug': ('title',)}









        # HOW TO AUTO SELECT USER FOR SAVING IN DJANGO ADMIN FORM
# class PostAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "author":
#             kwargs["queryset"] = get_user_model().objects.filter(
#                 username=request.user.username
#             )
#         return super(PostAdmin, self).formfield_for_foreignkey(
#             db_field, request, **kwargs
#         )

#     def get_readonly_fields(self, request, obj=None):
#         if obj is not None:
#             return self.readonly_fields + ("author",)
#         return self.readonly_fields

#     def add_view(self, request, form_url="", extra_context=None):
#         data = request.GET.copy()
#         data["author"] = request.user
#         request.GET = data
#         return super(NotesAdmin, self).add_view(
#             request, form_url="", extra_context=extra_context
#         )