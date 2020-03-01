from django.contrib import admin

#from karaokeapp.modules.profile.user_profile.models.user_profile_model import Profile
#from karaokeapp.modules.profile.user_profile.admin.user_profile_admin import 

from django.contrib.auth.models import User
admin.site.unregister(User)
from karaokeapp.modules.profile.user_profile.admin.user_profile_admin import CustomUserAdmin
admin.site.register(User, CustomUserAdmin)

from karaokeapp.modules.room.room_info.models.room_info_models import RoomStatus
from karaokeapp.modules.room.room_info.admin.room_info_admin import RoomStatusAdmin
admin.site.register(RoomStatus, RoomStatusAdmin)