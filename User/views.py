from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from User.models import *
from User import sendEmail
from django.http import JsonResponse


# Create your views here.
# def index(request):
#     return render(request, 'index.html')


# 注册
def sign_up(request):
    if request.method == "GET":
        return render(request, 'User/sign_up.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('inputEmail')
        password1 = request.POST.get('inputPassword')
        password2 = request.POST.get('inputPasswordConfirm')
        # verifyCode = request.POST.get('emailVerify')

        Reg_Dict = {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2,
        }

        user1 = User.objects.filter(email=email)
        user2 = User.objects.filter(name=username)

        if user1:
            Reg_Dict['register_err'] = "邮箱已经用于注册"
            return render(request, 'User/sign_up.html', Reg_Dict)
        elif user2:
            Reg_Dict['register_err'] = "用户名已存在"
            return render(request, 'User/sign_up.html', Reg_Dict)
        # elif 'verifyCode' not in request.session:
        #     Reg_Dict['register_err'] = "邮箱验证码已过期"
        #     return render(request, 'User/sign_up.html', Reg_Dict)
        # elif verifyCode != request.session['verifyCode'] and request.session['verifyCode'] != None and \
        #         request.session['username'] == username:
        #     Reg_Dict['register_err'] = "邮箱验证码不正确"
        #     return render(request, 'User/sign_up.html', Reg_Dict)

        else:
            User.objects.create(email=email, password=password1, name=username)
            return render(request, 'User/sign_in.html')


def email_verify(request):
    username = request.POST.get('username')
    email = request.POST.get('inputEmail')
    if not username:
        return JsonResponse(0, safe=False)
    elif not email:
        return JsonResponse(1, safe=False)
    else:
        verifycode = sendEmail.random_str()
        request.session['username'] = username
        request.session['verifyCode'] = verifycode
        request.session.set_expiry(100)
        sendEmail.send_register_email(email, verifycode, "register")
        return JsonResponse(2, safe=False)


# 登陆
def sign_in(request):
    if request.method == "GET":
        return render(request, 'User/sign_in.html')
    else:
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        user = User.objects.filter(email=email, password=password).first()
        # user = User.objects.get(email=email, password=password)

        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.name
            request.session['email'] = user.email
            request.session['authority'] = user.authority
            request.session.set_expiry(1000000)
            if user.authority == 1:
                return HttpResponseRedirect('/Manage')
            else:
                return HttpResponseRedirect('/index/')

        else:
            return render(request, 'User/sign_in.html', {'login_err': "用户名或密码错误"})


def sign_out(request):
    request.session.clear()
    return HttpResponseRedirect('/User/sign_in/')


def test(request):
    return render(request, 'User/sign_in.html')
