from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse
from Manage.models import Charge, Room, People


class ChargeManageTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.room = Room.objects.create(name='room1', desc='desc1', pic_url='pic1', video_url='video1')
        self.people = People.objects.create(name='lkx1', age=18, sex=0, job='hhh', response_room=self.room, desc='rew')
        self.charge1 = Charge.objects.create(name='name1', response_room=self.room, response_people=self.people,price=10)
        self.charge2 = Charge.objects.create(name='name2', response_room=self.room, response_people=self.people,price=10)


    def test_detail_charge_creat(self):
        print("This Case is:新建费用成功")
        url = reverse('Manage:charge_create')
        post = {'room_create':self.room.id,'people_create':self.people.id,'name': 'newName', 'response_room': self.room, 'response_people': self.people, 'price': 40}
        response = self.client.post(url, post)
        actualCharge = Charge.objects.all()
        self.assertEquals(len(actualCharge), 3)

    def test_detail_charge_update(self):
        print("This Case is:修改费用成功")
        charge_id = self.charge2.id
        url = reverse('Manage:charge_update')
        post = {'id': charge_id,
                'room_modify': self.room.id,
                'people_modify':self.people.id,
                'name': 'UpdateName',
                'response_room': self.room,
                'response_people': self.people,
                'price': 40}
        response = self.client.post(url, post)
        new_charge = Charge.objects.get(id=charge_id)
        self.assertEqual(new_charge.name, 'UpdateName')

    def test_detail_charge_delete(self):
        print("This Case is:删除费用成功")
        charge_id = self.charge1.id
        url = '/Manage/charge/delete/' + str(charge_id)
        actualCharge = Charge.objects.all()
        self.assertEquals(len(actualCharge), 2)