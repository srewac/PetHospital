from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response
from Test.models import *
from User.models import *
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
    if request.session.get('username', None):
        if request.session.get('test_id', None):
            test_id = request.session['test_id']
            user_name = request.session['username']
            selectedtest = Test.objects.get(id=test_id)
            question = Question.objects.filter(testpaper__test=test_id)
            choice = Choice.objects.filter(question__testpaper__test=test_id)
            if request.method =="GET":
                return render_to_response('Test/paper.html', locals())
            else:
                user_id = User.objects.get(name= user_name).id
                score = 0
                for question_id in question:
                    id = question_id.id
                    answer = request.POST.get(str(id))
                    c_answer = Choice.objects.get(id=answer)
                    c_score = Question.objects.get(id=id).score
                    if(c_answer.correct==True):
                        score += c_score
                    c_score = 0
                user_testscore = Usertest(user_id=user_id,test_id=test_id,score=score)
                user_testscore.save()
                del request.session['test_id']
                return HttpResponseRedirect('/Test/test/')
        else:
            return HttpResponseRedirect('/Test/test/')
    else:
        return HttpResponseRedirect(request,'/User/sign_in')