from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from User import models
from User import sendEmail
from django.http import JsonResponse


# Create your views here.
def index(request):
    if request.session.get('username', None):
        if request.session.get('authority', None) == 0:
            return render(request, 'index.html')
        else:
            return redirect(reverse('Manage:index', args=[]))
    else:
        return render(request, 'User/sign_in.html')

