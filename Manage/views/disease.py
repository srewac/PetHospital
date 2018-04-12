import json


from django.shortcuts import render, get_object_or_404
from Disease.models import DiseaseExample, Disease, Process, Picture, Video
from django.http import JsonResponse
from PIL import Image


# 进入病例管理界面
def disease_example(request):
    return render(request, 'backend/disease/disease_example_show.html')


# 进入新建病例界面
def disease_example_create_show(request):
    return render(request, 'backend/disease/disease_example_create.html')


# 进入病例详情界面
def disease_example_detail(request, disease_example_id):
    The_Dict = {
        'disease_example_id': disease_example_id
    }
    return render(request, 'backend/disease/disease_example_detail_show.html', The_Dict)


# 返回所有病例的简要信息
def disease_example_dict(request):
    disease_examples = DiseaseExample.objects.all()
    disease_example_d = {'data': []}
    for disease_ex in disease_examples:
        sub_disease = disease_ex.sub_disease
        disease = sub_disease.disease
        disease_example_d['data'].append([disease_ex.name, disease.name, sub_disease.name, disease_ex.id])
    return JsonResponse(disease_example_d, safe=False)


# 返回所选病例的详细信息
def disease_example_detail_dict(request, disease_example_id):
    disease_example = get_object_or_404(DiseaseExample, pk=disease_example_id)
    sub_disease = disease_example.sub_disease
    disease = sub_disease.disease
    PROCESSES = {}
    processes = disease_example.process_set.all()
    for process in processes:
        PICTURES = {}
        for pic in process.picture_set.all():
            PICTURES[str(pic.id)] = pic.pic_url
        VIDEOS = {}
        for video in process.video_set.all():
            VIDEOS[str(video.id)] = video.video_url
        process_d = {
            'process_name': process.name,
            'process_desc': process.desc,
            'process_pics': PICTURES,
            'process_videos': VIDEOS,
        }
        PROCESSES[str(process.id)] = process_d
    disease_example_detail_d = {
        'disease_example_name': disease_example.name,
        'disease_example_disease': disease.name,
        'disease_example_sub_disease': sub_disease.name,
        'disease_example_sub_disease_desc': sub_disease.desc,
        'disease_example_processes': PROCESSES,
    }
    return JsonResponse(json.dumps(disease_example_detail_d), safe=False)


# # 进入病例创建界面
# def disease_example_create(request):
#     return render(request, 'backend/disease/disease_example_create.html')


# 返回创建所需的信息
def disease_example_create_dict(request):
    DISEASES = {}
    SUBDISEASES = {}
    for disease in Disease.objects.all():
        DISEASES[str(disease.id)] = disease.name
        for sub_disease in disease.subdisease_set.all():
            SUBDISEASES[str(sub_disease.id)] = sub_disease.name
    dict = {
        'disease_all': DISEASES,
        'sub_disease_all': SUBDISEASES,
    }
    return JsonResponse(json.dumps(dict), safe=False)


# 创建病例，仅保存病例信息
def disease_example_create(request):
    check_disease_examples = DiseaseExample.objects.filter(name=request.POST['disease_example_name'])
    if len(check_disease_examples) > 0:
        return JsonResponse(False, safe=False)
    disease_example = DiseaseExample(name=request.POST['disease_example_name'],
                                     sub_disease_id=request.POST['subdisease'],
                                     )
    disease_example.save()
    return JsonResponse(disease_example.id, safe=False)


# 创建过程
def process_create(request):
    de_id = request.POST['process_disease_example_id']
    de = get_object_or_404(DiseaseExample, pk=de_id)
    check_processes = de.process_set.filter(name=request.POST['process_name'])
    if len(check_processes) > 0:
        return JsonResponse(False, safe=False)
    process = Process(name=request.POST['process_name'],
                      desc=request.POST['process_desc'],
                      disease_example_id=de_id,
                      )
    process.save()
    for f in request.FILES.getlist('process_pics'):
        file_name = f.temporary_file_path().split('\\')[-1]
        images_url = 'images/uploads/disease_example/images/' + file_name
        image = Image.open(f)
        image.save('/PetHospital/static/' + images_url)
        pic = Picture(pic_url=images_url,
                      process_id=process.id,
                      )
        pic.save()
    for v in request.FILES.getlist('process_videos'):
        video_name = v.temporary_file_path().split('\\')[-1]
        video_url = 'images/uploads/disease_example/videos/' + video_name

        video = Video(video_url=video_url,
                      process_id=process.id,
                      )
        video.save()
    return JsonResponse(de_id, safe=False)
