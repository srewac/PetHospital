from django.db import models
from Navigation.models import Room
from Disease.models import SubDisease


class People(models.Model):
    age = models.IntegerField()
    # 0->male, 1->female
    sex = models.IntegerField()
    name = models.CharField(max_length=30)
    job = models.CharField(max_length=50)
    response_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Charge(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    response_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    response_people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return '{} charges {}'.format(self.name, self.price)


class Analysis(models.Model):
    name = models.CharField(max_length=100)
    result = models.CharField(max_length=2000)
    response_people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField('due date')
    desc = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Inhospital(models.Model):
    patient = models.CharField(max_length=50)
    response_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    response_people = models.ForeignKey(People, on_delete=models.CASCADE)
    price = models.IntegerField()
    in_time = models.DateTimeField('in time')
    out_time = models.DateTimeField('out time')
    disease = models.ForeignKey(SubDisease, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient
