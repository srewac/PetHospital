from django.shortcuts import get_object_or_404, render, redirect
from Manage.models import People
from User.models import User
from django.urls import reverse
from django.http import JsonResponse

def people(request):
    peoples=People.objects.all()
    return render(request, 'backend/basic/people.html', {'users': users})