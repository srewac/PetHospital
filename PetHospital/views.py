from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from User import models
from User import sendEmail
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')
