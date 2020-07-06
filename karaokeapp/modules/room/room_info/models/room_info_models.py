from django.db import models
from django.contrib.auth.models import User
class RoomStatus(models.Model):
    status_name = models.CharField(max_length = 200, blank = True)
class Room(models.Model):
    name = models.CharField(max_length = 30, blank = False)
    user = models.ForeignKey(User, blank=True, null=True)
    status = models.ForeignKey(RoomStatus)
    note = models.CharField(max_length = 200, blank = True)
    start_time = models.DateField(null = True, blank = True)
    end_time = models.DateField(null = True, blank = True)
    insert_time = models.DateField(null = True, blank = True)
    update_time = models.DateField(null = True, blank = True)

    def __str__(self):  # __unicode__ for Python 2
        return self.name