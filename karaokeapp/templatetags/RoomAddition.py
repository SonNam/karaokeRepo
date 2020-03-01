from django import template
register = template.Library()
from karaokeapp.modules.room.room_info.models.room_info_models import RoomStatus

@register.inclusion_tag('room/add_room.html', takes_context= True)
def RoomAdditionTag(context):
    liststatuses = RoomStatus.objects.all()
    return {'liststatuses': liststatuses}