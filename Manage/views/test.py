from django.shortcuts import render
from Test.models import Question, TestPaper, Test
from django.http import JsonResponse
import Manage.utils as utils


def test_index(request):
    return render(request, 'backend/test/tables.html')


def testpapaer_index(request):
    return render(request, 'backend/test/tables.html')


def question_index(request):
    return render(request, 'backend/test/question_show.html', {'disease_all': utils.get_all_diseases()})


def question_dict(request):
    questions = Question.objects.all()
    questions_d = {'data': []}
    for question in questions:
        choice_text = ''
        correct_choice = None
        choices = question.choice_set.all()
        for i in range(len(choices)):
            choice_text = choice_text + str(i) + ":" + choices[i].text + ' '
            if choices[i].correct:
                correct_choice = choices[i]
        questions_d['data'].append(
            [question.text, choice_text, correct_choice.text, question.score, question.sub_disease.disease.name,
             question.sub_disease.name, question.id])
    return JsonResponse(questions_d, safe=False)


def get_all_diseases():
    disease_all = {}
    diseases = Disease.objects.all()
    for disease in diseases:
        disease_all[disease.name] = []
        sub_diseases = disease.subdisease_set.all()
        for sub_disease in sub_diseases:
            disease_all[disease.name].append(sub_disease)
    return disease_all
