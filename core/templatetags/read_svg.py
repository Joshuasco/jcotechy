from django.utils.safestring import mark_safe
from django import template
from django.contrib.sites.shortcuts import get_current_site
register = template.Library()
@register.simple_tag
def read_svg(file_name):
    file=open(file_name[1:]).read()
    return mark_safe(file)