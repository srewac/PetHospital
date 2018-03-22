from django.shortcuts import render
from Test.models import Question, TestPaper, Test, Choice
from Disease.models import Disease, SubDisease
from django.http import JsonResponse
import json


def test_index(request):
    return render(request, 'backend/test/tables.html')


def testpapaer_index(request):
    return render(request, 'backend/test/tables.html')


def question_index(request):
    return render(request, 'backend/test/question_show.html')


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


def sub_disease_dict(request, disease_id):
    disease = Disease.objects.get(id=disease_id)
    sub_diseases = disease.subdisease_set.all()
    sub_disease_d = {}
    for sub_disease in sub_diseases:
        sub_disease_d[str(sub_disease.id)] = sub_disease.name
    return JsonResponse(json.dumps(sub_disease_d), safe=False)


def question_create(request):
    question = Question(text=request.POST['question'],
                        score=request.POST['score'],
                        sub_disease_id=request.POST['sub_disease_selector'])
    question.save()
    question.choice_set.create(text=request.POST['choice1'], correct=(request.POST['correct_choice'] == 'choice1'))
    question.choice_set.create(text=request.POST['choice2'], correct=(request.POST['correct_choice'] == 'choice2'))
    question.choice_set.create(text=request.POST['choice3'], correct=(request.POST['correct_choice'] == 'choice3'))
    question.choice_set.create(text=request.POST['choice4'], correct=(request.POST['correct_choice'] == 'choice4'))
    return JsonResponse(True, safe=False)


def question_create_dict(request):
    DISEASES = {}
    SUBDISEASES = {}
    diseases = Disease.objects.all()
    sub_diseases = diseases[0].subdisease_set.all()
    for disease in diseases:
        DISEASES[str(disease.id)] = disease.name
    for sub_disease in sub_diseases:
        SUBDISEASES[str(sub_disease.id)] = sub_disease.name
    question_d = {
        'disease_all': DISEASES,
        'sub_disease_all': SUBDISEASES,
    }
    return JsonResponse(json.dumps(question_d), safe=False)


def question_modify(request):
    question = Question(text=request.POST['question'],
                        score=request.POST['score'],
                        sub_disease_id=request.POST['sub_disease_selector'])
    question.save()
    question.choice_set.create(text=request.POST['choice1'], correct=(request.POST['correct_choice'] == 'choice1'))
    question.choice_set.create(text=request.POST['choice2'], correct=(request.POST['correct_choice'] == 'choice2'))
    question.choice_set.create(text=request.POST['choice3'], correct=(request.POST['correct_choice'] == 'choice3'))
    question.choice_set.create(text=request.POST['choice4'], correct=(request.POST['correct_choice'] == 'choice4'))
    return JsonResponse(True, safe=False)


def question_modify_dict(request, question_id):
    question = Question.objects.get(id=question_id)
    DISEASES = {}
    SUBDISEASES = {}
    CHOICES = []
    diseases = Disease.objects.all()
    for disease in diseases:
        DISEASES[str(disease.id)] = disease.name
    sub_diseases = SubDisease.objects.filter(disease=question.sub_disease.disease)
    for sub_disease in sub_diseases:
        SUBDISEASES[str(sub_disease.id)] = sub_disease.name
    for choice in question.choice_set.all():
        CHOICES.append((choice.text, choice.correct))
    question_d = {
        'text': question.text,
        'score': question.score,
        'disease_all': DISEASES,
        'sub_disease_all': SUBDISEASES,
        'disease': question.sub_disease.disease_id,
        'sub_disease': question.sub_disease_id,
        'choices': CHOICES
    }
    return JsonResponse(json.dumps(question_d), safe=False)
