from django import forms 
from karaokeapp.modules.room.room_info.models.room_info_models import Room
  
class RoomForm(forms.ModelForm): 
    class Meta: 
        model = Room 
        fields = ['name', 'status', 'note',]