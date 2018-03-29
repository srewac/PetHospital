from django.test import TestCase
from django.test import Client
from django.urls import reverse
from Disease.models import Disease


class DiseaseManageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self_disease1 = Disease.objects.create(name='disease1')
        self_disease2 = Disease.objects.create(name='disease2')
        self_disease3 = Disease.objects.create(name='disease3')

    def test_detail_disease_example(self):
        print("This Case is:成功进入病例管理页面")
        response = self.client.get(reverse('Manage:disease_example_show'))
        self.assertEqual(response.status_code, 200)

    def test_detail_disease_information(self):
        print("This Case is:查看病例信息")
        response = self.client.get(reverse('Manage:disease_example_dict'))
        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(Disease.objects.all()),3)

    def test_detail_disease_create(self):
        print("This Case is:成功进入病例创建页面")
        response = self.client.get(reverse('Manage:disease_example_create'))
        self.assertEqual(response.status_code, 200)

