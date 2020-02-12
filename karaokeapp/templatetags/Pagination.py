'''
Created on 20 Jul 2019

@author: Ken
'''
from django import template
register = template.Library()

@register.inclusion_tag('mainpage/pagination.html', takes_context= True)
def PaginationTag(context, data):
    result = {}
    result['data'] = data
    return result