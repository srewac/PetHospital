from django.db import models


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    pic_url = models.CharField(max_length=500, default=None, blank=True)
    video_url = models.CharField(max_length=1000, default=None, blank=True)
    room_with_role = models.ManyToManyField(
        Role,
        through='Room_Role',
        through_fields=('room', 'role'),
    )

    def __str__(self):
        return self.name


class Room_Role(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return "room{}_role{}".format(self.room, self.role)
