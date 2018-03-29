from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse
from Manage.models import Medicine


class UserManageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.medicine1 = Medicine.objects.create(name='room1', desc='desc1', price=10)
        self.medicine2 = Medicine.objects.create(name='room2', desc='desc2', price=20)
        self.medicine3 = Medicine.objects.create(name='room3', desc='desc3', price=100)


    def test_detail_medicine_creat(self):
        print("This Case is:创建药品成功")
        url = reverse('Manage:medicine_create')
        post = {'name': 'newName', 'desc': 'newDesc','price': 40}
        response = self.client.post(url, post)
        actualRoom = Medicine.objects.all()
        self.assertEquals(len(actualRoom), 4)