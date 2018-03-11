from django.contrib import admin
from .models import Disease, SubDisease, GeneralProcess, DiseaseExample, Process

# Register your models here.
admin.site.register(Disease)
admin.site.register(SubDisease)
admin.site.register(GeneralProcess)
admin.site.register(DiseaseExample)
admin.site.register(Process)

