from django.shortcuts import get_object_or_404, render, redirect
from Manage.models import People, Charge
from User.models import User
from Navigation.models import Room
from django.urls import reverse
from django.http import JsonResponse
import json
from django.http import HttpResponse, HttpResponseRedirect


def charge(request):
    peoples = People.objects.all()
    rooms = Room.objects.all()
    charges = Charge.objects.all()
    The_Dict = {
        'peoples': peoples,
        'rooms': rooms,
        'charges': charges,
    }
    return render(request, 'backend/basic/charge.html', The_Dict)


def charge_dict(request):
    charges = Charge.objects.all()
    charge_d = {'data': []}
    for charge in charges:
        charge_d['data'].append(
            [charge.name, charge.price, charge.response_room.name, charge.response_people.name, charge.id,
             charge.response_room.id, charge.response_people.id])
    return JsonResponse(charge_d, safe=False)


def charge_delete(request, charge_id):
    charge = get_object_or_404(Charge, pk=charge_id)
    charge.delete()
    return JsonResponse(True, safe=False)


def modify_charge_init(request, people_id):
    people = People.objects.get(id=people_id)
    peoples = People.objects.filter(response_room=people.response_room)
    dict_people = []
    for people in peoples:
        temp = []
        temp.append(people.id)
        temp.append(people.name)
        dict_people.append(temp)
    return JsonResponse(dict_people, safe=False)


def modify_charge_room_select(request):
    room = Room.objects.get(id=request.POST['room_modify'])
    peoples = People.objects.filter(response_room=room)
    dict_people = []
    for people in peoples:
        temp = []
        temp.append(people.id)
        temp.append(people.name)
        dict_people.append(temp)
    return JsonResponse(dict_people, safe=False)


def charge_update(request):
    charge = get_object_or_404(Charge, pk=request.POST['id'])
    room = Room.objects.get(id=request.POST['room_modify'])
    response_people = People.objects.get(id=request.POST['people_modify'])
    charge.name = request.POST['name']
    charge.price = request.POST['price']
    charge.response_room = room
    charge.response_people = response_people
    charge.save()

    return JsonResponse(True, safe=False)


def create_charge_room_select(request):
    room = Room.objects.get(id=request.POST['room_create'])
    peoples = People.objects.filter(response_room=room)
    dict_people = []
    for people in peoples:
        temp = []
        temp.append(people.id)
        temp.append(people.name)
        dict_people.append(temp)
    return JsonResponse(dict_people, safe=False)


def charge_create(request):
    room = Room.objects.get(id=request.POST['room_create'])
    response_people = People.objects.get(id=request.POST['people_create'])
    charge = Charge(name=request.POST['name'],
                    price=request.POST['price'],
                    response_room=room,
                    response_people=response_people)
    charge.save()
    return JsonResponse(True, safe=False)
