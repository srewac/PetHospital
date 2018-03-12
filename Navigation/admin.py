from django.contrib import admin
from .models import Role, Room, Room_Role
# Register your models here.

admin.site.register(Role)
admin.site.register(Room)
admin.site.register(Room_Role)

