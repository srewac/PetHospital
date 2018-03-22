from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from Navigation.models import Room, Role


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
        room_d['data'].append([room.name, room.pic_url, room.video_url, room.desc, rs, room.id])
    return JsonResponse(room_d, safe=False)


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
    room.name = request.POST['name']
    room.pic_url = request.POST['pic']
    room.video_url = request.POST['video']
    room.desc = request.POST['desc']
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
        room = Room(name=request.POST['name'],
                    pic_url=request.POST['pic'],
                    video_url=request.POST['video'],
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
    room.delete()
    return JsonResponse(True, safe=False)
