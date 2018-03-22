from django.shortcuts import render, get_object_or_404
from Test.models import Question, TestPaper, Test, Choice
from Disease.models import Disease, SubDisease
from django.http import JsonResponse
import json


# 进入考场管理
def test_index(request):
    return render(request, 'backend/test/tables.html')


# 进入考卷管理
def testpapaer_index(request):
    return render(request, 'backend/test/tables.html')


# 进入考题管理
def question_index(request):
    return render(request, 'backend/test/question_show.html')


# 返回所有考题
def question_dict(request):
    questions = Question.objects.all()
    questions_d = {'data': []}
    for question in questions:
        correct_choice = None
        assert (len(question.choice_set.all()) == 4)
        choices = question.choice_set.all()
        choice_text = 'A.' + choices[0].text + ' ' + 'B.' + choices[1].text + ' ' + 'C.' + choices[
            2].text + ' ' + 'D.' + choices[3].text
        for i in range(len(choices)):
            if choices[i].correct:
                correct_choice = choices[i]
        questions_d['data'].append(
            [question.text, choice_text, correct_choice.text, question.score, question.sub_disease.disease.name,
             question.sub_disease.name, question.id])
    return JsonResponse(questions_d, safe=False)


# 根据disease_id返回所有此类下的subdisease
def sub_disease_dict(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    sub_diseases = disease.subdisease_set.all()
    sub_disease_d = {}
    for sub_disease in sub_diseases:
        sub_disease_d[str(sub_disease.id)] = sub_disease.name
    return JsonResponse(json.dumps(sub_disease_d), safe=False)


# 创建question
def question_create(request):
    question = Question(text=request.POST['question'],
                        score=request.POST['score'],
                        sub_disease_id=request.POST['sub_disease_selector'])
    question.save()
    assert request.POST['choice1'] is not None
    question.choice_set.create(text=request.POST['choice1'], correct=(request.POST['correct_choice'] == 'choice1'))
    assert request.POST['choice2'] is not None
    question.choice_set.create(text=request.POST['choice2'], correct=(request.POST['correct_choice'] == 'choice2'))
    assert request.POST['choice3'] is not None
    question.choice_set.create(text=request.POST['choice3'], correct=(request.POST['correct_choice'] == 'choice3'))
    assert request.POST['choice4'] is not None
    question.choice_set.create(text=request.POST['choice4'], correct=(request.POST['correct_choice'] == 'choice4'))
    return JsonResponse(True, safe=False)


# 返回创建问题时要用到的disease和subdisease列表
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


# 修改问题
def question_modify(request):
    assert request.POST['id'] is not None
    question = get_object_or_404(Question, pk=request.POST['id'])
    question.text = request.POST['question']
    question.score = request.POST['score']
    question.sub_disease_id = request.POST['sub_disease_selector']
    assert (len(question.choice_set.all()) == 4)
    question.choice_set.all().delete()
    assert request.POST['choice1'] is not None
    question.choice_set.create(text=request.POST['choice1'], correct=(request.POST['correct_choice'] == 'choice1'))
    assert request.POST['choice2'] is not None
    question.choice_set.create(text=request.POST['choice2'], correct=(request.POST['correct_choice'] == 'choice2'))
    assert request.POST['choice3'] is not None
    question.choice_set.create(text=request.POST['choice3'], correct=(request.POST['correct_choice'] == 'choice3'))
    assert request.POST['choice4'] is not None
    question.choice_set.create(text=request.POST['choice4'], correct=(request.POST['correct_choice'] == 'choice4'))
    question.save()
    return JsonResponse(True, safe=False)


# 返回问题修改时要显示的原数据
def question_modify_dict(request, question_id):
    question = get_object_or_404(Question, id=question_id)
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
        'id': question.id,
        'text': question.text,
        'score': question.score,
        'disease_all': DISEASES,
        'sub_disease_all': SUBDISEASES,
        'disease': question.sub_disease.disease_id,
        'sub_disease': question.sub_disease_id,
        'choices': CHOICES
    }
    return JsonResponse(json.dumps(question_d), safe=False)


# 删除问题
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return JsonResponse(True, safe=False)
