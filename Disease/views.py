from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response
from Test.models import TestPaper
from Disease.models import Disease

def select_disease(request):
    if request.method == "GET":
        testpaper = TestPaper.objects.all()
        disease = Disease.objects.all()
        return render_to_response('Disease/disease.html', locals())

def select_subdisease(request, disease):
        return render(request,'Test/index.html')