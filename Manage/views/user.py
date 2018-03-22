from django.shortcuts import get_object_or_404, render, redirect
from User.models import User
from django.urls import reverse
from django.http import JsonResponse


# 进入用户管理界面
def index(request):
    users = User.objects.all()
    return render(request, 'backend/user/user_info.html', {'users': users})


# 返回所有账户信息
def user_dict(request):
    users = User.objects.all()
    user_d = {'data': []}
    for user in users:
        user_d['data'].append([user.email, user.name, user.password, '实习生' if user.authority == 0 else '管理员', user.id])
    return JsonResponse(user_d, safe=False)


# 用户删除
def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return JsonResponse(True, safe=False)


# 用户修改
def user_update(request):
    user = get_object_or_404(User, pk=request.POST['id'])
    check_users = User.objects.filter(email=request.POST['email'])
    if len(check_users) > 0:
        for check_user in check_users:
            if check_user.email != user.email:
                return JsonResponse(False, safe=False)
    user.email = request.POST['email']
    user.name = request.POST['name']
    user.password = request.POST['password']
    user.authority = request.POST['authority']
    user.save()
    return JsonResponse(True, safe=False)


# 用户创建
def user_create(request):
    check_user = User.objects.filter(email=request.POST['email'])
    if len(check_user) > 0:
        return JsonResponse(False, safe=False)
    else:
        user = User(email=request.POST['email'],
                    name=request.POST['name'],
                    password=request.POST['password'],
                    authority=request.POST['authority'])
        user.save()
        return JsonResponse(True, safe=False)
