'''
Created on 5 Aug 2018

@author: Ken
'''
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from karaokeapp.modules.room.room_info.views.room_info_views import listRoomInfo, addRoomInfo
urlpatterns = [
    url(r'^listRoomInfo/$', listRoomInfo, name='karaokeapp.listRoomInfo'),
    url(r'^addRoomInfo/$', addRoomInfo, name='karaokeapp.addRoomInfo'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)