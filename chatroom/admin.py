from django.contrib import admin
from chatroom.models import Room, Message
#from .models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)