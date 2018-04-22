from django.db import models
from Disease.models import Disease, SubDisease
import datetime
from django.utils import timezone


class Question(models.Model):
    text = models.CharField(max_length=1000)
    score = models.IntegerField(default=2)
    sub_disease = models.ForeignKey(SubDisease, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestPaper(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=1000)
    questions = models.ManyToManyField(Question)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def get_full_score(self):
        full_score = 0
        for question in self.questions.all():
            full_score = full_score + question.score
        return full_score

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=500)
    duration = models.IntegerField(default=60)  # 考试时间
    close_time = models.DateTimeField('close date')
    start_time = models.DateTimeField('start date')
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE)

    # 考试状态 0->考试未开始，1->考试进行中，2->考试已结束
    def test_status(self):
        if timezone.now() < self.start_time:
            return 0
        elif timezone.now() > self.close_time:
            return 2
        else:
            return 1

    def __str__(self):
        return self.name
