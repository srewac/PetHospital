from django.shortcuts import render
from django.contrib import auth
from User import models

# Create your views here.
def index(request):
    return render(request, 'User/sign_in.html')

def sign_up(request):
    return render(request,'User/sign_up.html')

def sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        obj = models.User.objects.get(email=email)
        passwd_db = obj.password
        name = obj.name
    except:
        return render(request, 'User/sign_in.html', {'login_err': "用户名或密码错误"})
    if password == passwd_db:
        request.session['username']= name
        request.session.set_expiry(600)
        return render(request,'Test/test.html')
    else:
        return render(request, 'User/sign_in.html', {'login_err': "用户名或密码错误"})
