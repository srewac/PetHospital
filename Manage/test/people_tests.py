from Manage.models import People,Room
from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse


class PeopleManageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.room = Room.objects.create(name='room1', desc='desc1', pic_url='pic1', video_url='video1')
        self.people1 = People.objects.create(name='lkx1', age=18, sex=0, job='hhh', response_room=self.room.name, desc='rew')
        self.people2 = People.objects.create(name='lkx2', age=5, sex=1, job='ooo', response_room=self.room.name, desc='tre')
        self.people3 = People.objects.create(name='lkx3', age=3, sex=0, job='lll', response_room=self.room.name, desc='uytr')

    def test_detail_room_creat(self):
        print("This Case is:新增人员成功")
        url = reverse('Manage:people_create')
        post = {'name': 'newName', 'age': 19, 'sex': 0, 'job': 'jjj', 'response_room': self.room.name, 'desc': 'fs'}
        response = self.client.post(url, post)
        actualPeople = People.objects.all()
        self.assertEquals(len(actualPeople), 4)
