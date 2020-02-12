'''
Created on 2 Jul 2019

@author: Ken
'''
from django import template
register = template.Library()

@register.inclusion_tag('mainpage/navigation.html', takes_context= True)
def NavigationTag(context):
    result = {}
    return result