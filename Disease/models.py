from django.db import models


# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SubDisease(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=1000)
    pic_url = models.CharField(max_length=500, default=None, blank=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GeneralProcess(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    sub_disease = models.ForeignKey(SubDisease, on_delete=models.CASCADE)

    def __str__(self):
        return self.desc


class Index(models.Model):
    name = models.CharField(max_length=50)
    reference_num = models.IntegerField(default=0)
    sub_disease = models.ForeignKey(SubDisease, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DiseaseExample(models.Model):
    name = models.CharField(max_length=100)
    sub_disease = models.ForeignKey(SubDisease, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    disease_example = models.ForeignKey(DiseaseExample, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Picture(models.Model):
    pic_url = models.CharField(max_length=500)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    def __str__(self):
        return self.pic_url


class Video(models.Model):
    video_url = models.CharField(max_length=500)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_url
