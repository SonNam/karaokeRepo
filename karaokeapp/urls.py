'''
Created on 5 Aug 2018

@author: Ken
'''
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)