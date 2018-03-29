from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse
from User.models import User


# Create your tests here.
class UserManageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.user1 = User.objects.create(email='admin1@example.com', password='admin1', name='admin1', authority=1)
        self.user2 = User.objects.create(email='admin2@example.com', password='admin2', name='admin2', authority=1)
        self.user3 = User.objects.create(email='user1@example.com', password='user1', name='user1', authority=0)
        self.user4 = User.objects.create(email='user2@example.com', password='user2', name='user2', authority=0)

    def test_detail_user_index(self):
        print("This Case is:成功进入用户管理页面")
        response = self.client.get(reverse('Manage:user_show'))
        self.assertEqual(response.status_code, 200)

    def test_detail_user_data(self):
        print("This Case is:获取全部用户信息")
        url = reverse('Manage:user_dict')
        response = self.client.post(url)
        actualUser = User.objects.all()
        self.assertEquals(len(actualUser), 4)

    def test_detail_delete_user(self):
        print("This Case is:删除用户成功")
        user_id = self.user1.id
        url = '/Manage/user/delete/' + str(user_id)
        response = self.client.get(url)

        actualUser = User.objects.all()
        self.assertEquals(len(actualUser), 3)

    #嘤不会写写不出
    def test_detail_update_user(self):
        print("This Case is:修改用户成功")
        id = self.user1.id
        url = reverse('Manage:user_update')
        post = {'user_id': id}
        response = self.client.post(url + str(id))
        actualUser = User.objects.all()

    def test_detail_create_user(self):
        print("This Case is:创建用户成功")
        url = reverse('Manage:user_create')
        post = {'email': 'newuser@example.com', 'name': 'newname', 'password': 'newpassword', 'authority': 1}
        response = self.client.post(url, post)
        actualUser = User.objects.all()
        self.assertEquals(len(actualUser), 5)
