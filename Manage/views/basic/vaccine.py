from datetime import timedelta, datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from Manage.models import Vaccine


def vaccine(request):
    return render(request, 'backend/basic/vaccine.html')


def vaccine_dict(request):
    vaccines = Vaccine.objects.all()
    vaccine_d = {'data': []}
    for vaccine in vaccines:
        vaccine_d['data'].append([vaccine.name, vaccine.due_date.strftime('%Y-%m-%d'), vaccine.desc, vaccine.id])
    return JsonResponse(vaccine_d, safe=False)


# 修改疫苗信息
def vaccine_modify(request):
    vaccine = get_object_or_404(Vaccine, pk=request.POST['id'])
    check_vaccines = Vaccine.objects.filter(name=request.POST['name'])
    if len(check_vaccines) > 0:
        for check_vaccine in check_vaccines:
            if check_vaccine.name != vaccine.name:
                return JsonResponse(False, safe=False)
    vaccine.name = request.POST['name']
    vaccine.due_date = datetime.strptime(request.POST['due_date'], "%Y-%m-%d")
    vaccine.desc = request.POST['desc']
    vaccine.save()
    return JsonResponse(True, safe=False)


# 新建疫苗
def vaccine_create(request):
    check_vaccine = Vaccine.objects.filter(name=request.POST['name'])
    if len(check_vaccine) > 0:
        return JsonResponse(False, safe=False)
    else:
        vaccine = Vaccine(name=request.POST['name'],
                          # 由于系统默认0点为前一天所以对天数做加一操作
                          due_date=datetime.strptime(request.POST['due_date'], "%Y-%m-%d"),
                          desc=request.POST['desc'])
        vaccine.save()
    return JsonResponse(True, safe=False)


#删除疫苗
def vaccine_delete(request, vaccine_id):
    vaccine = get_object_or_404(Vaccine, pk=vaccine_id)
    vaccine.delete()
    return JsonResponse(True, safe=False)
