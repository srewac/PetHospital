from django.shortcuts import get_object_or_404, render, redirect
from Manage.models import People
from User.models import User
from Navigation.models import Room
from django.urls import reverse
from django.http import JsonResponse


def people(request):
    peoples = People.objects.all()
    rooms = Room.objects.all()
    The_Dict = {
        'peoples': peoples,
        'rooms': rooms,
    }
    return render(request, 'backend/basic/people.html', The_Dict)


def people_dict(request):
    peoples = People.objects.all()
    people_d = {'data': []}
    for people in peoples:
        people_d['data'].append(
            [people.name, people.age, '男' if people.sex == 0 else '女', people.job, people.response_room.name,
             people.desc, people.id])
    return JsonResponse(people_d, safe=False)


def people_delete(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    people.delete()
    return JsonResponse(True, safe=False)


def people_update(request):
    people = get_object_or_404(People, pk=request.POST['id'])
    room = request.POST['room']
    response_room = Room.objects.get(name=room)

    people.name = request.POST['name']
    people.age = request.POST['age']
    if request.POST['sex'] == "男":
        people.sex = 0
    else:
        people.sex = 1
    people.job = request.POST['job']
    people.response_room=response_room
    people.desc=request.POST['desc']
    people.save()

    return JsonResponse(True, safe=False)


def people_create(request):
    room = request.POST['room']
    response_room = Room.objects.get(name=room)
    if request.POST['sex'] == "男":
        sex = 0
    else:
        sex = 1
    people = People(name=request.POST['name'],
                    age=request.POST['age'],
                    sex=sex,
                    job=request.POST['job'],
                    response_room=response_room,
                    desc=request.POST['desc'])
    people.save()
    return JsonResponse(True, safe=False)
