from Manage.models import Vaccine
from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse


class VaccineManageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.vaccine1 = Vaccine.objects.create(name='name1', due_date='2018-03-29', desc='desc1')
        self.vaccine2 = Vaccine.objects.create(name='name2', due_date='2018-04-29', desc='desc2')

    def test_detail_vaccine_index(self):
        print("This Case is:成功进入疫苗管理页面")
        response = self.client.get(reverse('Manage:vaccine_show'))
        self.assertEqual(response.status_code, 200)

    def test_detail_vaccine_data(self):
        print("This Case is:获取全部疫苗信息")
        url = reverse('Manage:vaccine_dict')
        response = self.client.post(url)
        actualVacine = Vaccine.objects.all()
        self.assertEquals(len(actualVacine), 2)

    def test_detail_update_vaccine(self):
        print("This Case is:修改疫苗信息成功")
        vaccine_id = self.vaccine2.id
        url = reverse('Manage:vaccine_modify')
        post = {'id':vaccine_id,'name':'updateName', 'due_date':'2018-03-29', 'desc':'desc1'}
        response = self.client.post(url, post)
        new_vaccine = Vaccine.objects.get(id=vaccine_id)
        self.assertEqual(new_vaccine.name, 'updateName')

    def test_detail_create_vaccine(self):
        print("This Case is:创建疫苗成功")
        url = reverse('Manage:vaccine_create')
        post = {'name':'NewName', 'due_date':'2018-03-30', 'desc':'NewDesc'}
        response = self.client.post(url, post)
        actualVaccine = Vaccine.objects.all()
        self.assertEquals(len(actualVaccine), 3)


    def test_detail_delete_vaccine(self):
        print("This Case is:删除疫苗成功")
        vaccine_id = self.vaccine1.id
        url = '/Manage/vaccine/delete/' + str(vaccine_id)
        response = self.client.get(url)

        actualUser = Vaccine.objects.all()
        self.assertEquals(len(actualUser), 2)
