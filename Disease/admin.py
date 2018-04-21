from django.contrib import admin
from .models import Disease, SubDisease, GeneralProcess, DiseaseExample, Process, Picture, Video


class SubDiseaseInline(admin.TabularInline):
    model = SubDisease
    extra = 5


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [SubDiseaseInline]


class GeneralProcessInline(admin.TabularInline):
    model = GeneralProcess
    extra = 1


class SubDiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'disease')
    list_filter = ('disease',)
    inlines = [GeneralProcessInline]


class ProcessInlined(admin.TabularInline):
    model = Process
    extra = 5


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 1


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'disease_example')
    inlines = [PictureInline, VideoInline]


class DiseaseExampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sub_disease')
    inlines = [ProcessInlined]


# admin.site.register(Disease)
admin.site.register(SubDisease, SubDiseaseAdmin)
admin.site.register(Disease, DiseaseAdmin)
# admin.site.register(GeneralProcess)
admin.site.register(DiseaseExample, DiseaseExampleAdmin)
# admin.site.register(Process)
admin.site.register(Process, ProcessAdmin)
