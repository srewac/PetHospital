from django.test import TestCase, RequestFactory
from django.test import Client
from User.models import User
from django.urls import reverse
import time


# Create your tests here.
class UserTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_details_sign_in(self):
        print("This Case is：登录成功")

        email = 'admin1@example.com'
        password = 'admin1'
        name = 'admin1'
        post = {'email': email, 'password': password}
        url = reverse('sign_in')
        self.user = User.objects.create(email=email, password=password, name=name)
        response = self.client.post(url, post)
        self.assertEqual(response.status_code, 200)

        actualUser = User.objects.filter(email=email, password=password).first()
        self.assertEquals(actualUser.email, email)
        self.assertEquals(actualUser.password, password)
        self.assertEqual(actualUser.name, name)

    def test_details_error_sign_in(self):
        print("This Case is：密码错误，登录失败")

        email = 'admin1@example.com'
        password = 'admin1'
        name = 'admin1'
        post = {'email': email, 'password': password}
        url = reverse('sign_in')
        self.user = User.objects.create(email=email, password='123', name=name)
        response = self.client.post(url, post)
        self.assertContains(response, "用户名或密码错误")

    def test_details_verifyCode_error_sign_up(self):
        print("This Case is：邮箱验证码不正确，注册失败")

        email = 'admin2@example.com'
        password = 'admin2'
        name = 'admin2'
        authority = 1
        session = self.client.session
        session['verifyCode'] = '123'
        session['username'] = name
        session['email'] = email
        session['authority'] = authority
        session.set_expiry(100)
        session.save()
        post = {'username': name, 'inputEmail': email, 'inputPassword': password, 'inputPasswordConfirm': password,
                'emailVerify': '1234'}

        url = reverse('sign_up')
        response = self.client.post(url, post)

        self.assertContains(response, "邮箱验证码不正确")

    def test_details_verfiyCode_due_sign_up(self):
        print("This Case is：邮箱验证码已过期,注册失败")

        email = 'admin2@example.com'
        password = 'admin2'
        name = 'admin2'
        authority = 1
        verifyCode = 123
        session = self.client.session
        session['verifyCode'] = verifyCode
        session['username'] = name
        session['email'] = email
        session['authority'] = authority
        session.set_expiry(1)
        session.save()
        post = {'username': name, 'inputEmail': email, 'inputPassword': password, 'inputPasswordConfirm': password,
                'emailVerify': verifyCode}
        url = reverse('sign_up')
        time.sleep(2)

        response = self.client.post(url, post)

        self.assertContains(response, "邮箱验证码已过期")

    def test_details_exist_email_sign_up(self):
        print("This Case is：邮箱已经用于注册,注册失败")

        email = 'admin2@example.com'
        password = 'admin2'
        name = 'admin2'
        authority = 1
        verifyCode = 123

        session = self.client.session
        session['verifyCode'] = verifyCode
        session['username'] = name
        session['email'] = email
        session['authority'] = authority
        session.set_expiry(100)
        session.save()
        post = {'username': name, 'inputEmail': email, 'inputPassword': password, 'inputPasswordConfirm': password,
                'emailVerify': verifyCode}
        url = reverse('sign_up')

        self.user = User.objects.create(email=email, password=password)
        response = self.client.post(url, post)

        self.assertContains(response, "邮箱已经用于注册")

    def test_details_exist_username_sign_up(self):
        print("This Case is：用户名已存在,注册失败")

        email = 'admin2@example.com'
        password = 'admin2'
        name = 'admin2'
        authority = 1
        verifyCode = 123

        session = self.client.session
        session['verifyCode'] = verifyCode
        session['username'] = name
        session['email'] = email
        session['authority'] = authority
        session.set_expiry(100)
        session.save()
        post = {'username': name, 'inputEmail': email, 'inputPassword': password, 'inputPasswordConfirm': password,
                'emailVerify': verifyCode}
        url = reverse('sign_up')

        self.user = User.objects.create(password=password, name=name)
        response = self.client.post(url, post)

        self.assertContains(response, "用户名已存在")