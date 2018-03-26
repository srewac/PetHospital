from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response
from Test.models import *
from Disease.models import Disease


# Create your views here.
def test(request):
    if request.session.get('username', None):
        return render(request, 'Test/test.html')
    else:
        return HttpResponseRedirect('/User/sign_in/')

def select_paper(request, disease_name):
    if request.session.get('username', None):
        if request.method == "GET":
            disease = Disease.objects.get(name=disease_name)
            #testpaper = disease.testpaper_set.all()
            test = Test.objects.filter(test_paper__disease__name=disease_name)
            #testpaper = TestPaper.objects.filter(disease=disease)
            return render_to_response('Test/select_paper.html', locals())
    else:
        return HttpResponseRedirect('/User/sign_in/')


def select_disease(request):
    if request.session.get('username', None):
        if request.method == "GET":
            testpaper = TestPaper.objects.all()
            disease = Disease.objects.all()
            return render_to_response('Test/select_disease.html', locals())
    else:
        return HttpResponseRedirect('/User/sign_in/')

def selected_paper(request):
    test_id = request.POST.get('test_id')
    request.session['test_id'] = test_id
    return render(request, 'Test/test.html')

def paper(request):
    if request.session.get('test_id', None):
        if request.method =="GET":
            test_id = request.session['test_id']
            selectedtest = Test.objects.get(id=test_id)
            choice = Choice.objects.filter(question__testpaper__test=test_id)
            return render_to_response('Test/paper.html', locals())
        else:
            del request.session['test_id']
            #TODO: submit answers
            return HttpResponseRedirect('/Test/test/')
    else:
        return HttpResponseRedirect('/Test/test/')
