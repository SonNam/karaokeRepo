from django.contrib import admin

class RoomStatusAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super(RoomStatusAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (None, {
                'fields': ('status_name',)
            }),
        )    
    list_display  = ('status_name',)