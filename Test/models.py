from django.db import models


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=1000)
    score = models.IntegerField(default=2)

    def __str__(self):
        return Question.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class TestPaper(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=1000)
    testpaper_with_question = models.ManyToManyField(
        Question,
        through='TestPaper_Question',
        through_fields=('testpaper', 'question'),
    )

    def get_full_score(self):
        pass

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=500)
    duration = models.IntegerField(default=60) #考试时间
    close_time = models.DateTimeField('close date')
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TestPaper_Question(models.Model):
    testpaper = models.ForeignKey(TestPaper, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "testpaper{}_question{}".format(self.testpaper, self.question)
