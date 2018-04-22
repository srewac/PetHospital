from django.shortcuts import render, render_to_response, HttpResponseRedirect
from Navigation.models import Room
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json


# Create your views here.
def hall(request):
    if request.session.get('username', None):
        return render(request, 'Navigation/hall.html')
    else:
        return HttpResponseRedirect('/User/sign_in/')


def TwoD_Navigation(request):
    if request.session.get('username', None):
        rooms = Room.objects.all()
        return render(request, 'Navigation/TwoD_Navigation.html', locals())
    else:
        return HttpResponseRedirect('/User/sign_in/')


def TwoD_getRooms(request, room_id):
    room = Room.objects.get(id=room_id)
    room_d = {'room_name': room.name,
              'room_desc': room.desc}
    return JsonResponse(json.dumps(room_d), safe=False)


def ward(request):
    if request.session.get('username', None):
        return render(request, 'Navigation/ward.html')

    else:
        return HttpResponseRedirect('/User/sign_in/')
