from django.contrib import admin
from .models import Question, TestPaper, Choice, Test, TestPaper_Question
# Register your models here.

admin.site.register(Question)
admin.site.register(TestPaper)
admin.site.register(Choice)
admin.site.register(Test)
admin.site.register(TestPaper_Question)
