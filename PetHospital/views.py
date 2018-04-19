from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from User import models
from User import sendEmail
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

