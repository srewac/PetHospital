from django.shortcuts import render


def index(request):
    return render(request, 'backend/user/tables.html')
