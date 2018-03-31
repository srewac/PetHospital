from Manage.models import Analysis, People,Room
from django.test import TestCase,RequestFactory
from django.test import Client
from django.urls import reverse

class DiseaseManageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.room = Room.objects.create(name='room1', desc='desc1', pic_url='pic1', video_url='video1')
        self.people = People.objects.create(name='lkx1', age=18, sex=0, job='hhh', response_room=self.room, desc='rew')
        self.analysis1 = Analysis.objects.create(name='analysis_name1', result='result1', response_people=self.people)
        self.analysis2 = Analysis.objects.create(name='analysis_name2', result='result2', response_people=self.people)


    def test_detail_analysis_creat(self):
        print("This Case is:新建化验单成功")
        url = reverse('Manage:analysis_create')
        post = {'people_name':self.people.name,'analysis_name': 'newName', 'analysis_result': 'newResult', 'response_people': self.people}
        response = self.client.post(url, post)
        actualRoom = Analysis.objects.all()
        self.assertEquals(len(actualRoom), 3)

    def test_detail_analysis_delete(self):
        print("This Case is:删除化验单成功")
        analysis_id = self.analysis1.id
        url = '/Manage/analysis/delete/' + str(analysis_id)
        actualAnalysis = Analysis.objects.all()
        self.assertEquals(len(actualAnalysis), 2)
