import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from datetime import timedelta, datetime

from Disease.models import SubDisease, Disease
from Manage.models import Inhospital, People
from Navigation.models import Room


def inhospital(request):
    peoples = People.objects.all()
    rooms = Room.objects.all()
    diseases = Disease.objects.all

    The_dict = {
        'peoples': peoples,
        'rooms': rooms,
        'diseases': diseases,
    }
    return render(request, 'backend/basic/inhospital.html', The_dict)


# 获取住院列表
def inhospital_dict(request):
    patients = Inhospital.objects.all()
    patient_d = {'data': []}
    for patient in patients:
        people = get_object_or_404(People, pk=patient.response_people_id)
        room = get_object_or_404(Room, pk=patient.response_room_id)
        subdisease = get_object_or_404(SubDisease, pk=patient.sub_disease_id)
        disease = get_object_or_404(Disease, pk=subdisease.disease_id)
        patient_d['data'].append([patient.patient, patient.price, patient.in_time.strftime('%Y-%m-%d'),
                                  patient.out_time.strftime('%Y-%m-%d'),
                                  people.name, room.name, disease.name, subdisease.name, patient.id])
    return JsonResponse(patient_d, safe=False)


# 返回修改时要显示的原数据
def inhospital_modify_dict(request, id):
    patient = get_object_or_404(Inhospital, pk=id)
    PEOPLES = {}
    ROOMS = {}
    DISEASES = {}
    SUBDISEASES = {}
    peoples = People.objects.all()
    rooms = Room.objects.all()
    diseases = Disease.objects.all()
    for people in peoples:
        PEOPLES[str(people.id)] = people.name
    for room in rooms:
        ROOMS[str(room.id)] = room.name
    for disease in diseases:
        DISEASES[str(disease.id)] = disease.name
    sub_diseases = SubDisease.objects.filter(disease=patient.sub_disease.disease)
    for sub_disease in sub_diseases:
        SUBDISEASES[str(sub_disease.id)] = sub_disease.name
    patient_d = {
        'id': patient.id,
        'patient': patient.patient,
        'price': patient.price,
        'in_time': patient.in_time.strftime('%Y-%m-%d'),
        'out_time': patient.out_time.strftime('%Y-%m-%d'),
        'people_all': PEOPLES,
        'room_all': ROOMS,
        'disease_all': DISEASES,
        'sub_disease_all': SUBDISEASES,
        'people': patient.response_people_id,
        'room': patient.response_room_id,
        'disease': patient.sub_disease.disease_id,
        'sub_disease': patient.sub_disease_id,
    }
    return JsonResponse(json.dumps(patient_d), safe=False)


# 修改住院信息
def inhospital_modify(request):
    patients = get_object_or_404(Inhospital, pk=request.POST['id'])
    check_patients = Inhospital.objects.filter(patient=request.POST['patient'])
    if len(check_patients) > 0:
        for check_patient in check_patients:
            if check_patient.patient != patients.patient:
                return JsonResponse(False, safe=False)
    patients.patient = request.POST['patient']
    patients.price = request.POST['price']
    patients.in_time = datetime.strptime(request.POST['in_time'], "%Y-%m-%d")
    patients.out_time = datetime.strptime(request.POST['out_time'], "%Y-%m-%d")
    patients.response_people_id = request.POST['people_name']
    patients.response_room_id = request.POST['room_name']
    patients.sub_disease_id = request.POST['subdisease']
    patients.save()
    return JsonResponse(True, safe=False)


# 返回创建时所需的列表数据
def inhospital_create_dict(request):
    PEOPLES = {}
    ROOMS = {}
    DISEASES = {}
    SUBDISEASES = {}
    peoples = People.objects.all()
    rooms = Room.objects.all()
    diseases = Disease.objects.all()
    sub_diseases = diseases[0].subdisease_set.all()
    for people in peoples:
        PEOPLES[str(people.id)] = people.name
    for room in rooms:
        ROOMS[str(room.id)] = room.name
    for disease in diseases:
        DISEASES[str(disease.id)] = disease.name
    for sub_disease in sub_diseases:
        SUBDISEASES[str(sub_disease.id)] = sub_disease.name
    inhospital_d = {
        'people_all': PEOPLES,
        'room_all': ROOMS,
        'disease_all': DISEASES,
        'sub_disease_all': SUBDISEASES,
    }
    return JsonResponse(json.dumps(inhospital_d), safe=False)


# 创建
def inhospital_create(request):
    patient = Inhospital(patient=request.POST['patient'],
                         price=request.POST['price'],
                         in_time=datetime.strptime(request.POST['in_time'], "%Y-%m-%d"),
                         out_time=datetime.strptime(request.POST['out_time'], "%Y-%m-%d"),
                         response_people_id=request.POST['people_name'],
                         response_room_id=request.POST['room_name'],
                         sub_disease_id=request.POST['subdisease'],
    )
    patient.save()
    return JsonResponse(True, safe=False)


# 删除
def inhospital_delete(request, patient_id):
    patient = get_object_or_404(Inhospital, pk=patient_id)
    patient.delete()
    return JsonResponse(True, safe=False)
