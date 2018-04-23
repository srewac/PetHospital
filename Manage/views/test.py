from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from Test.models import Question, TestPaper, Test, Choice
from Disease.models import Disease, SubDisease
from User.models import User, Usertest, Usertest_question

import json, datetime


# 进入考题管理
def question_index(request):
    return render(request, 'backend/test/question_show.html')


# 进入考卷生成
def testpaper_create_show(request):
    return render(request, 'backend/test/testpaper_create_show.html', )


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
def disease_sub_disease_dict(request):
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


# 创建考卷详情
def testpaper_create(request):
    testpaper = TestPaper(name=request.POST['name'],
                          desc=request.POST['desc'],
                          disease_id=request.POST['disease'])
    testpaper.save()
    return JsonResponse(testpaper.id, safe=False)


# 考卷选择考题
def select_question(request, testpaper_id):
    testpaper = get_object_or_404(TestPaper, pk=testpaper_id)
    score_all = testpaper.get_full_score()
    return render(request, 'backend/test/select_question.html',
                  {'testpaper_id': str(testpaper_id),
                   'score_all': score_all,
                   'testpaper_name': testpaper.name,
                   'disease': testpaper.disease.name
                   })


# 选择某一病类的考题
def select_question_dict(request, testpaper_id):
    testpaper = get_object_or_404(TestPaper, pk=testpaper_id)
    questions = Question.objects.filter(sub_disease__disease=testpaper.disease)
    questions_d = {'data': []}
    for question in questions:
        question_in_testpaper = '1' if question in testpaper.questions.all() else '0'
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
             question.sub_disease.name, str(question.id) + ';' + question_in_testpaper])
    return JsonResponse(questions_d, safe=False)


# 为试卷添加考题
def testpaper_question_add(request, testpaper_id, question_id):
    testpaper = TestPaper.objects.get(pk=testpaper_id)
    question = Question.objects.get(pk=question_id)
    if question in testpaper.questions.all():
        return JsonResponse(False, safe=False)
    else:
        testpaper.questions.add(question)
        return JsonResponse(True, safe=False)


# 为试卷删除考题
def testpaper_question_delete(request, testpaper_id, question_id):
    testpaper = TestPaper.objects.get(pk=testpaper_id)
    question = Question.objects.get(pk=question_id)
    if question in testpaper.questions.all():
        testpaper.questions.remove(question)
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)


# 清空某张试卷全部试题
def testpaper_question_delete_all(request, testpaper_id):
    testpaper = TestPaper.objects.get(pk=testpaper_id)
    for question in testpaper.questions.all():
        testpaper.questions.remove(question)
    return JsonResponse(True, safe=False)


# 进入考卷管理
def testpaper_index(request):
    diseases = Disease.objects.all()
    disease_d = {}
    for disease in diseases:
        disease_d[disease.id] = disease.name
    return render(request, 'backend/test/testpaper_show.html', disease_d)


# 获取所有试卷简要信息
def testpaper_dict(request):
    testpapers = TestPaper.objects.all()
    testpaper_d = {'data': []}
    for testpaper in testpapers:
        testpaper_d['data'].append(
            [testpaper.name, testpaper.desc, testpaper.disease.name, testpaper.get_full_score(), testpaper.id])
    return JsonResponse(testpaper_d, safe=False)


# 删除试卷
def testpaper_delete(request, testpaper_id):
    testpaper = get_object_or_404(TestPaper, pk=testpaper_id)
    testpaper.delete()
    return JsonResponse(True, safe=False)


# 修改试卷页面获取原始数据
def testpaper_modify_dict(request, testpaper_id):
    testpaper = get_object_or_404(TestPaper, pk=testpaper_id)
    testpaper_d = {
        'name': testpaper.name,
        'desc': testpaper.desc,
        'disease': testpaper.disease.id
    }
    return JsonResponse(json.dumps(testpaper_d), safe=False)


# 修改试卷信息操作
def testpaper_modify(request):
    testpaper = get_object_or_404(TestPaper, pk=request.POST['id'])
    testpaper.name = request.POST['name']
    testpaper.desc = request.POST['desc']
    if testpaper.disease_id != int(request.POST['disease']):
        for question in testpaper.questions.all():
            testpaper.questions.remove(question)
        testpaper.disease = get_object_or_404(Disease, pk=request.POST['disease'])
    testpaper.save()
    return JsonResponse(True, safe=False)


# 进入考场管理
def test_index(request):
    testpapers_d = {}
    for testpaper in TestPaper.objects.all():
        testpapers_d[testpaper.id] = testpaper.name
    return render(request, 'backend/test/test_show.html', {'testpapers': testpapers_d})


# 获取所有考场信息
def test_dict(request):
    tests = Test.objects.all()
    test_d = {'data': []}
    for test in tests:
        status = test.test_status()
        status_d = ''
        if status == 0:
            status_d = "未开始"
        elif status == 1:
            status_d = "进行中"
        elif status == 2:
            status_d = "已结束"
        start_date = str(test.start_time.date())
        start_time = str(test.start_time.time()).split(':')[0] + ':' + str(test.start_time.time()).split(':')[1]
        close_date = str(test.close_time.date())
        close_time = str(test.close_time.time()).split(':')[0] + ':' + str(test.close_time.time()).split(':')[1]
        test_d['data'].append([test.name,
                               test.test_paper.name,
                               test.duration,
                               start_date + ' ' + start_time,
                               close_date + ' ' + close_time,
                               status_d,
                               test.id])
    return JsonResponse(test_d, safe=False)


# 创建考场（返回0表示考试时长未负，返回1表示结束时间输入不全，返回2表示结束日期早于当前时间，返回3表示一起正常）
def test_create(request):
    # 如果考试时间为负或大于300，返回0
    if int(request.POST['duration']) < 0 or int(request.POST['duration']) > 300:
        return JsonResponse(0, safe=False)
    # 获取时间
    close_time = str(request.POST['close_time'])
    start_time = str(request.POST['start_time'])
    # 如果开始时间不全，返回1
    if start_time == '':
        return JsonResponse(1, safe=False)
    # 如果结束时间不全，返回2
    if close_time == '':
        return JsonResponse(2, safe=False)
    # 如果结束时间年份过大，返回3
    close_year = [int(v) for v in close_time.replace('T', '-').replace(':', '-').split('-')][0]
    if close_year > 3000:
        return JsonResponse(3, safe=False)
    # 如果结束时间年份过大，返回4
    start_year = [int(v) for v in start_time.replace('T', '-').replace(':', '-').split('-')][0]
    if start_year > 3000:
        return JsonResponse(4, safe=False)
    # 如果结束时间小于当前时间，返回5
    processed_start_date = datetime.datetime(
        *[int(v) for v in start_time.replace('T', '-').replace(':', '-').split('-')])
    if processed_start_date <= timezone.now():
        return JsonResponse(5, safe=False)
    # 如果结束时间小于当前时间，返回6
    processed_close_date = datetime.datetime(
        *[int(v) for v in close_time.replace('T', '-').replace(':', '-').split('-')])
    if processed_close_date <= timezone.now():
        return JsonResponse(6, safe=False)
    # 如果结束时间小于开始时间，返回7
    if processed_close_date <= processed_start_date:
        return JsonResponse(7, safe=False)
    # 如果一切正常进行添加操作，返回8
    test = Test(name=request.POST['name'],
                test_paper_id=request.POST['testpaper'],
                duration=request.POST['duration'],
                start_time=processed_start_date,
                close_time=processed_close_date)
    test.save()
    for user in User.objects.filter(authority=0).all():
        test.user_set.add(user)
    return JsonResponse(8, safe=False)


# 修改考场前获取初始信息
def test_modify_dict(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    test_d = {
        'name': test.name,
        'duration': test.duration,
        'testpaper': test.test_paper_id,
        'start_time': str(test.start_time).replace(' ', 'T'),
        'close_time': str(test.close_time).replace(' ', 'T'),
        'status': test.test_status(),
    }
    return JsonResponse(json.dumps(test_d), safe=False)


# 修改考场
def test_modify(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    # 如果考试时间为负或大于300，返回0
    if int(request.POST['duration']) < 0 or int(request.POST['duration']) > 300:
        return JsonResponse(0, safe=False)
    # 如果开始时间不全，返回1
    if test.test_status() == 0:
        start_time = str(request.POST['start_time'])
    else:
        start_time = test.start_time
    if start_time == '':
        return JsonResponse(1, safe=False)
    # 如果结束时间不全，返回2
    close_time = str(request.POST['close_time'])
    if close_time == '':
        return JsonResponse(2, safe=False)
    # 如果结束时间年份过大，返回3
    close_year = [int(v) for v in close_time.replace('T', '-').replace(':', '-').split('-')][0]
    if close_year > 3000:
        return JsonResponse(3, safe=False)
    # 如果开始时间年份过大，返回4
    if test.test_status() == 0:
        start_year = [int(v) for v in start_time.replace('T', '-').replace(':', '-').split('-')][0]
        if start_year > 3000:
            return JsonResponse(4, safe=False)
    # 如果结束时间小于当前时间，返回5
    if test.test_status() == 0:
        processed_start_date = datetime.datetime(
            *[int(v) for v in start_time.replace('T', '-').replace(':', '-').split('-')])
        if processed_start_date <= timezone.now():
            return JsonResponse(5, safe=False)
    else:
        processed_start_date = start_time
    # 如果结束时间小于当前时间，返回6
    processed_close_date = datetime.datetime(
        *[int(v) for v in close_time.replace('T', '-').replace(':', '-').split('-')])
    if processed_close_date <= timezone.now():
        return JsonResponse(6, safe=False)
    # 如果结束时间小于开始时间，返回7
    if processed_close_date <= processed_start_date:
        return JsonResponse(7, safe=False)
    # 如果一切正常进行添加操作，返回8
    if test.test_status() == 0:
        test.name = request.POST['name']
        test.duration = request.POST['duration']
        test.test_paper_id = request.POST['testpaper']
        test.start_time = processed_start_date
        test.close_time = processed_close_date
        test.save()
        return JsonResponse(8, safe=False)
    elif test.test_status() == 1:
        test.name = request.POST['name']
        test.duration = request.POST['duration']
        test.close_time = processed_close_date
        test.save()
        return JsonResponse(8, safe=False)
    else:
        # 正常情况无法进入这种情况
        return JsonResponse(9, safe=False)


# 删除考场
def test_delete(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    for test_taker in test.user_set.all():
        for usertest in test_taker.usertest_set.all():
            usertest.delete()
        test.user_set.remove(test_taker)
    test.delete()
    return JsonResponse(True, safe=False)


# 显示考场所有考生
def test_detail_show(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    status = ''
    if test.test_status() == 0:
        status = "未开始"
    elif test.test_status() == 1:
        status = "进行中"
    else:
        status = "已结束"
    test_d = {'test_id': test.id, 'test_name': test.name, 'test_status': status}
    return render(request, 'backend/test/test_detail_show.html', test_d)


# 考场详情显示所有考生获取的数据
def test_detail_dict(request, test_id):
    test_origin = get_object_or_404(Test, pk=test_id)
    all_interns = User.objects.filter(authority=0).all()
    users = test_origin.user_set.all()
    all_interns_d = {'data': []}
    # 最后一个数据返回 0->未加入考试，1->加入考试;用户的user_id
    for all_intern in all_interns:
        if all_intern in users:
            usertest = Usertest.objects.filter(user=all_intern, test=test_origin).all()
            if len(usertest) == 1:
                all_interns_d['data'].append(
                    [all_intern.email, all_intern.name, usertest.first().score, '1;' + str(all_intern.id)])
            else:
                all_interns_d['data'].append([all_intern.email, all_intern.name, '无成绩', '1;' + str(all_intern.id)])
        else:
            if test_origin.test_status() == 0:
                all_interns_d['data'].append([all_intern.email, all_intern.name, '无成绩', '0;' + str(all_intern.id)])
    return JsonResponse(all_interns_d, safe=False)


# 考场添加考生
def test_detail_add_user(request, test_id, user_id):
    get_object_or_404(User, id=user_id).tests.add(get_object_or_404(Test, id=test_id))
    return JsonResponse(True, safe=False)


# 考场删除考生
def test_detail_delete_user(request, test_id, user_id):
    get_object_or_404(User, id=user_id).tests.remove(get_object_or_404(Test, id=test_id))
    return JsonResponse(True, safe=False)


# 考场添加所有实习生
def test_detail_add_all_user(request, test_id):
    # 初始化清空
    test = get_object_or_404(Test, pk=test_id)
    for user in test.user_set.all():
        test.user_set.remove(user)
    # 全部加入
    interns = User.objects.filter(authority=0).all()
    for intern in interns:
        intern.tests.add(test)
    return JsonResponse(True, safe=False)


# 考场删除所有实习生
def test_detail_delete_all_user(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    for user in test.user_set.all():
        test.user_set.remove(user)
    return JsonResponse(True, safe=False)

