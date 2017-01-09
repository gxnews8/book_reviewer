from django import template
from ..models import Book,Review

register = template.Library()
# each template tags module needs to contain variable called register
    # to be valid tag library
# 'register' used to register your own template tags and library
# to register w/ diff name : @register.simple_tag(name='my_tag')
