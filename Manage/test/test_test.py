# from django.test import TestCase, RequestFactory
# from django.test import Client
# from django.urls import reverse
#
#
# class TestManageTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     # TODO:功能太多暂时未写全
#     def test_detail_question_index(self):
#         print("This Case is:成功进入考题管理页面")
#         response = self.client.get(reverse('Manage:question_show'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_detail_question_create_show(self):
#         print("This Case is:成功进入考题生成页面")
#         response = self.client.get(reverse('Manage:question_create'))
#         self.assertEqual(response.status_code, 200)
