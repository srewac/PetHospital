from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, Http404, render_to_response
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
            user_name = request.session['username']
            user = User.objects.get(name=user_name)
            disease = Disease.objects.get(name=disease_name)
            now = datetime.datetime.now()
            test = user.tests.filter(test_paper__disease_id=disease.id).all()
            test = test.exclude(usertest__user_id=user.id)
            test = test.exclude(close_time__lt=now)
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
            user_id = request.session['user_id']
            selectedtest = Test.objects.get(id=test_id)
            questiones = Question.objects.filter(testpaper__test=test_id)
            choice = Choice.objects.filter(question__testpaper__test=test_id)
            if request.method == "GET":
                return render_to_response('Test/paper.html', locals())
            else:
                score = 0
                user_testscore = Usertest(user_id=user_id, test_id=test_id, score=score)
                user_testscore.save()
                for question in questiones:
                    answer = request.POST.get(str(question.id))
                    c_score = Question.objects.get(id=question.id).score
                    user_testscore_id = user_testscore.id
                    question_id = question.id
                    if answer == None:
                        t_answer = question.choice_set.get(correct=1).id
                        question_testscore = Usertest_question(usertest_id=user_testscore_id,
                                                               question_id=question_id,
                                                               score=0, userchoice_id=t_answer)
                        question_testscore.save()
                    else:
                        c_answer = Choice.objects.get(id=answer)
                        if c_answer.correct == False:
                            question_testscore = Usertest_question(usertest_id=user_testscore_id,
                                                                   question_id=question_id,
                                                                   score=0, userchoice_id=answer)
                            question_testscore.save()
                        elif c_answer.correct == True:
                            question_testscore = Usertest_question(usertest_id=user_testscore_id,
                                                                   question_id=question_id,
                                                                   score=c_score, userchoice_id=answer)
                            question_testscore.save()
                            score += c_score
                user_testscore.score = score
                user_testscore.save()
                del request.session['test_id']
                return HttpResponseRedirect('/Test/test/')
        else:
            return HttpResponseRedirect('/Test/test/')
    else:
        return HttpResponseRedirect(request, '/User/sign_in')


def result(request):
    if request.session.get('username', None):
        user_id = request.session['user_id']
        result = Usertest.objects.filter(user=user_id)
        return render_to_response('Test/result.html', locals())
    else:
        return HttpResponseRedirect('/User/sign_in')


def result_detail(request, test_id):
    if request.session.get('user_id', None):
        test_id = test_id
        user_id = request.session['user_id']
        questions = Question.objects.filter(testpaper__test=test_id)
        choices = Choice.objects.filter(question__testpaper__test=test_id)
        usertest_question = Usertest_question.objects.filter(usertest__test=test_id)
        user_choices = [a.userchoice_id for a in usertest_question]
        return render_to_response('Test/result_detail.html', locals())
    else:
        return HttpResponseRedirect('/User/sign_in')
