from django.shortcuts import render
from Disease.models import Disease, SubDisease, DiseaseExample
from django.http import JsonResponse


def index(request):
    return render(request, 'backend/disease/disease_show.html', {'disease_all': get_all_diseases()})


def disease_example(request):
    return render(request, 'backend/disease/disease_example_show.html')


def disease_example_dict(request):
    disease_examples = DiseaseExample.objects.all()
    disease_example_d = {'data': []}
    for disease_ex in disease_examples:
        sub_disease = disease_ex.sub_disease
        disease = sub_disease.disease
        disease_example_d['data'].append([disease_ex.name, disease.name, sub_disease.name, disease_ex.id])
    return JsonResponse(disease_example_d, safe=False)


def disease_example_create(request):
    return render(request, 'backend/disease/disease_example_create.html')


def get_all_diseases():
    disease_all = {}
    diseases = Disease.objects.all()
    for disease in diseases:
        disease_all[disease.name] = []
        sub_diseases = disease.subdisease_set.all()
        for sub_disease in sub_diseases:
            disease_all[disease.name].append(sub_disease)
    return disease_all
