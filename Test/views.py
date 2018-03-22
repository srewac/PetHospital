from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response
from django.template import loader
from Test.models import TestPaper
from Disease.models import Disease



# Create your views here.
def test(request):
    # if request.session.get('username', None):
    return render(request, 'Test/test.html')
    # else:
        # return render(request, 'User/sign_in.html')

def select_paper(request, disease_name):
    if request.method == "GET":
        disease = Disease.objects.get(name=disease_name)
        testpaper = TestPaper.objects.filter(disease=disease)
        return render_to_response('Test/select_paper.html',locals())
    else:
        paper = request.POST.get('selectedpaper')
        #TODO: page for single test
        return render(request,'User/index.html')

def select_disease(request):
    if request.method == "GET":
        testpaper = TestPaper.objects.all()
        disease = Disease.objects.all()
        return render_to_response('Test/select_disease.html',locals())


def test_management(request):
    return render(request, 'Test/test_management.html')