'''
Created on 3 Jul 2019

@author: Ken
'''
from django import template
register = template.Library()

@register.inclusion_tag('mainpage/coppyright.html', takes_context= True)
def CoppyRightTag(context):
    result = {}
    return result