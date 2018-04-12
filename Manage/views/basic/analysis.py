from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from Manage.models import Analysis, People


def analysis(request):
    peoples = People.objects.all()
    The_Dict = {
        'peoples': peoples,
    }
    return render(request, 'backend/basic/analysis.html', The_Dict)


# 获取化验列表
def analysis_dict(request):
    analysises = Analysis.objects.all()
    analysis_d = {'data': []}
    for analysis in analysises:
        people = get_object_or_404(People, pk=analysis.response_people_id)
        analysis_d['data'].append([analysis.name, analysis.result, people.name, analysis.id])
    return JsonResponse(analysis_d, safe=False)


# 新建化验
def analysis_create(request):
    check_analysis = Analysis.objects.filter(name=request.POST['analysis_name'])
    if len(check_analysis) > 0:
        return JsonResponse(False, safe=False)
    people = People.objects.get(name=request.POST['people_name'])
    analysis = Analysis(name=request.POST['analysis_name'],
                        result=request.POST['analysis_result'],
                        response_people=people)
    analysis.save()
    return JsonResponse(True, safe=False)


# 删除化验
def analysis_delete(request, analysis_id):
    analysis = get_object_or_404(Analysis, pk=analysis_id)
    analysis.delete()
    return JsonResponse(True, safe=False)

