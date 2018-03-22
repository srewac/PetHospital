from django.shortcuts import render

def room(request):
    return render(request, 'backend/basic/room.html')
