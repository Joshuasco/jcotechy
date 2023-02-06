from django.utils.safestring import mark_safe
from django import template
from django.contrib.sites.shortcuts import get_current_site
register = template.Library()
@register.simple_tag
def read_svg(file_name):
    print("#########################")
    print(f"----------{file_name}------------")
    index_no=file_name.index('media')
    actual_file=file_name[index_no:]
    print(actual_file)
    file=open(actual_file).read()
    return mark_safe(file)