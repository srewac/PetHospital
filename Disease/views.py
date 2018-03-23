from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response
from Test.models import TestPaper
from Disease.models import Disease
from Disease.models import SubDisease

def select_disease(request):
    if request.session.get('username', None):
        if request.method == "GET":
            testpaper = TestPaper.objects.all()
            disease = Disease.objects.all()
            return render_to_response('Disease/disease.html', locals())
    else:
        return HttpResponseRedirect('/User/sign_in')


def select_subdisease(request, disease_name):
    if request.session.get('username', None):
        if request.method == "GET":
            print(disease_name)
            disease = Disease.objects.get(name=disease_name)
            subdisease = disease.subdisease_set.all()
            return render_to_response('Disease/subdisease.html', locals())
    else:
        return HttpResponseRedirect('/User/sign_in/');
