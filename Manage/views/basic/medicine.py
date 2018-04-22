from django.shortcuts import get_object_or_404, render, redirect
from Manage.models import People, Medicine
from User.models import User
from Navigation.models import Room
from django.urls import reverse
from django.http import JsonResponse


def medicine(request):
    medicines = Medicine.objects.all()
    The_Dict = {
        'medicines': medicines,
    }
    return render(request, 'backend/basic/medicine.html', The_Dict)


def medicine_dict(request):
    medicines = Medicine.objects.all()
    medicine_d = {'data': []}
    for medicine in medicines:
        medicine_d['data'].append(
            [medicine.name, medicine.desc, medicine.price, medicine.id])
    return JsonResponse(medicine_d, safe=False)


def medicine_delete(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    medicine.delete()
    return JsonResponse(True, safe=False)


def medicine_update(request):
    medicine = get_object_or_404(Medicine, pk=request.POST['id'])
    medicine.name = request.POST['name']
    medicine.desc = request.POST['desc']
    medicine.price = request.POST['price']
    medicine.save()

    return JsonResponse(True, safe=False)


def medicine_create(request):
    medicine = Medicine(name=request.POST['name'],
                        desc=request.POST['desc'],
                        price=request.POST['price'])
    medicine.save()
    return JsonResponse(True, safe=False)
