from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse
from Navigation.models import Room, Role


class UserManageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.room1 = Room.objects.create(name='room1', desc='desc1', pic_url='pic1', video_url='video1')
        self.room2 = Room.objects.create(name='room2', desc='desc2', pic_url='pic2', video_url='video2')
        self.room3 = Room.objects.create(name='room3', desc='desc3', pic_url='pic3', video_url='video3')

    def test_detail_room_creat(self):
        print("This Case is:创建科室成功")
        url = reverse('Manage:room_create')
        post = {'name': 'newName', 'desc': 'newDesc','pic': 'newPic', 'video': 'newVideo'}
        response = self.client.post(url, post)
        actualRoom = Room.objects.all()
        self.assertEquals(len(actualRoom), 4)

    def test_detail_room_delete(self):
        print("This Case is:创建科室成功")
        url = reverse('Manage:room_create')
        post = {'name': 'newName', 'desc': 'newDesc','pic': 'newPic', 'video': 'newVideo'}
        response = self.client.post(url, post)
        actualRoom = Room.objects.all()
        self.assertEquals(len(actualRoom), 4)
