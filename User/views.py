from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from User import models


# Create your views here.
def index(request):
    return render(request, 'User/index.html')


# 注册
def sign_up(request):
    if request.method == "GET":
        return render(request, 'User/index.html')
    else:
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        user1 = models.User.objects.filter(email=email)
        user2 = models.User.objects.filter(name=username)
        if user1:
            return HttpResponse('该邮箱已经被注册，请更换邮箱')
        else:
            if user2:
                return HttpResponse('该用户名已经被使用，请更换名称')
            else:
                models.User.objects.create(email=email, password=password1, name=username)
                return render(request, 'User/index.html')


# 登陆
def sign_in(request):
    if request.method == "GET":
        return render(request, 'User/index.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = models.User.objects.get(email=email, password=password)
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.name
            request.session['email'] = user.email
            request.session.set_expiry(600)
            return HttpResponseRedirect('/User/index/')
        else:
            return render(request, 'User/index.html', {'login_err': "用户名或密码错误"})

def sign_out(request):
    request.session.clear();
    return HttpResponseRedirect('/User/index/');
