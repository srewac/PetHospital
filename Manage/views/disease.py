from django.shortcuts import render
from Disease.models import Disease, SubDisease, DiseaseExample
from django.http import JsonResponse


# 进入病例管理界面
def disease_example(request):
    return render(request, 'backend/disease/disease_example_show.html')


# 返回所有病例的简要信息
def disease_example_dict(request):
    disease_examples = DiseaseExample.objects.all()
    disease_example_d = {'data': []}
    for disease_ex in disease_examples:
        sub_disease = disease_ex.sub_disease
        disease = sub_disease.disease
        disease_example_d['data'].append([disease_ex.name, disease.name, sub_disease.name, disease_ex.id])
    return JsonResponse(disease_example_d, safe=False)


# 进入病例创建界面
def disease_example_create(request):
    return render(request, 'backend/disease/disease_example_create.html')
