import json
import os
import shutil

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from Navigation.models import Room, Role
from PetHospital.settings import STATIC_ROOT


def room(request):
    return render(request, 'backend/basic/room.html')


# 获取科室列表
def room_dict(request):
    rooms = Room.objects.all()
    room_d = {'data': []}
    for room in rooms:
        rs = ''
        for room_role in room.roles.all():
            role = get_object_or_404(Role, pk=room_role.id)
            rs = rs + role.name + ' '
        room_d['data'].append([room.name, room.desc, rs, room.id])
    return JsonResponse(room_d, safe=False)


# 获取修改时科室信息
def room_modify_dict(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    room_info = {'name': room.name,
                 'pic_url': room.pic_url,
                 'video_url': room.video_url,
                 'desc': room.desc,
                 }
    return JsonResponse(json.dumps(room_info), safe=False)


# 修改科室
def room_modify(request):
    room = get_object_or_404(Room, pk=request.POST['id'])
    for r in room.roles.all():
        room.roles.remove(r)
    check_rooms = Room.objects.filter(name=request.POST['name'])
    if len(check_rooms) > 0:
        for check_room in check_rooms:
            if check_room.name != room.name:
                return JsonResponse(False, safe=False)
    images_url = 'images/uploads/room/images/'
    video_url = 'images/uploads/room/videos/'
    # create path
    pic_path = STATIC_ROOT + 'images/uploads/room/images'
    video_path = STATIC_ROOT + 'images/uploads/room/videos'
    if not os.path.exists(pic_path):
        os.makedirs(pic_path)
    if not os.path.exists(video_path):
        os.makedirs(video_path)

    room.name = request.POST['name']
    room.desc = request.POST['desc']

    if len(request.FILES.getlist('room_pics')) > 0:
        if room.pic_url is not None:
            os.remove(STATIC_ROOT + room.pic_url)
        for f in request.FILES.getlist('room_pics'):
            pic_name = f.temporary_file_path().replace('\\', '/').split('/')[-1]
            images_url = images_url + pic_name
            shutil.copy(f.temporary_file_path(), STATIC_ROOT + images_url)
        room.pic_url = images_url

    if len(request.FILES.getlist('room_videos')) > 0:
        if room.video_url is not None:
            os.remove(STATIC_ROOT + room.video_url)
        for f in request.FILES.getlist('room_videos'):
            video_name = f.temporary_file_path().replace('\\', '/').split('/')[-1]
            video_url = video_url + video_name
            shutil.copy(f.temporary_file_path(), STATIC_ROOT + video_url)
        room.video_url = video_url
    room.save()
    if 'proscenium' in request.POST.keys():
        role = get_object_or_404(Role, pk=1)
        room.roles.add(role)
    if 'assistant' in request.POST.keys():
        role = get_object_or_404(Role, pk=2)
        room.roles.add(role)
    if 'veterinary_practitioner' in request.POST.keys():
        role = get_object_or_404(Role, pk=3)
        room.roles.add(role)
    return JsonResponse(True, safe=False)


# 创建科室
def room_create(request):
    check_room = Room.objects.filter(name=request.POST['name'])
    if len(check_room) > 0:
        return JsonResponse(False, safe=False)
    else:
        images_url = 'images/uploads/room/images/'
        video_url = 'images/uploads/room/videos/'
        pic_path = STATIC_ROOT + 'images/uploads/room/images'
        if not os.path.exists(pic_path):
            os.makedirs(pic_path)
        for f in request.FILES.getlist('room_pics'):
            pic_name = f.temporary_file_path().replace('\\', '/').split('/')[-1]
            images_url = images_url + pic_name
            shutil.copy(f.temporary_file_path(), STATIC_ROOT + images_url)
        video_path = STATIC_ROOT + 'images/uploads/room/videos'
        if not os.path.exists(video_path):
            os.makedirs(video_path)
        for f in request.FILES.getlist('room_videos'):
            video_name = f.temporary_file_path().replace('\\', '/').split('/')[-1]
            video_url = video_url + video_name
            shutil.copy(f.temporary_file_path(), STATIC_ROOT + video_url)
        room = Room(name=request.POST['name'],
                    pic_url=images_url,
                    video_url=video_url,
                    desc=request.POST['desc'])
        room.save()
        if 'proscenium' in request.POST.keys():
            role = get_object_or_404(Role, pk=1)
            room.roles.add(role)
        if 'assistant' in request.POST.keys():
            role = get_object_or_404(Role, pk=2)
            room.roles.add(role)
        if 'veterinary_practitioner' in request.POST.keys():
            role = get_object_or_404(Role, pk=3)
            room.roles.add(role)
        return JsonResponse(True, safe=False)


# 删除科室
def room_delete(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    for r in room.roles.all():
        room.roles.remove(r)
    if room.pic_url is not None:
        os.remove(STATIC_ROOT + room.pic_url)
    if room.video_url is not None:
        os.remove(STATIC_ROOT + room.video_url)
    room.delete()
    return JsonResponse(True, safe=False)
