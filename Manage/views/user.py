from django.shortcuts import get_object_or_404, render, redirect
from User.models import User
from django.urls import reverse
from django.http import JsonResponse


def index(request):
    users = User.objects.all()
    return render(request, 'backend/user/user_info.html', {'users': users})


def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect(reverse('Manage:user_show'))
    # return JsonResponse([user_id], safe=False)


def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.email = request.POST['email']
    user.name = request.POST['name']
    user.password = request.POST['password']
    user.authority = request.POST['authority']
    user.save()
    user_dict = {'id': user.id,
                 'email': user.email,
                 'name': user.name,
                 'password': user.password,
                 'authority': user.authority}
    return JsonResponse(user_dict)
