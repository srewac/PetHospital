from django.contrib import admin
from .models import Role, Room


# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc');


admin.site.register(Role)
admin.site.register(Room, RoomAdmin)
