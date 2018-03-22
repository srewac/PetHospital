# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404
# from Navigation.models import Room, Role, Room_Role
#
#
# def room(request):
#     return render(request, 'backend/basic/room.html')
#
#
# def room_dict(request):
#     rooms = Room.objects.all()
#     room_d = {'data': []}
#     for room in rooms:
#         room_roles = Room_Role.objects.filter(room_id=room.id)
#         roles = ''
#         for room_role in room_roles:
#             role = get_object_or_404(Role, pk=room_role.role_id)
#             roles = roles + role.name + ' '
#         room_d['data'].append([room.name, room.pic_url, room.video_url, room.desc, roles, room.id])
#     return JsonResponse(room_d, safe=False)
#
#
# def room_modify(request):
#     room = get_object_or_404(Room, pk=request.POST['id'])
#     check_rooms = Room.objects.filter(name=request.POST['name'])
#     if len(check_rooms) > 0:
#         for check_room in check_rooms:
#             if check_room.name != room.name:
#                 return JsonResponse(False, safe=False)
#     room.name = request.POST['name']
#     room.pic_url = request.POST['pic']
#     room.video_url = request.POST['video']
#     room.desc = request.POST['desc']
#     room.save()
#     return JsonResponse(True, safe=False)
#
#
# def room_create(request):
#     check_room = Room.objects.filter(name=request.POST['name'])
#     if len(check_room) > 0:
#         return JsonResponse(False, safe=False)
#     else:
#         room = Room(name=request.POST['name'],
#                     pic_url=request.POST['pic'],
#                     video_url=request.POST['video'],
#                     desc=request.POST['desc'])
#         room.save()
#         return JsonResponse(True, safe=False)
#
#
# def room_delete(request, room_id):
#     room = get_object_or_404(Room, pk=room_id)
#     room.delete()
#     return JsonResponse(True, safe=False)
