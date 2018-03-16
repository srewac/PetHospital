from django.contrib import admin
from .models import Question, TestPaper, Choice, Test, TestPaper_Question
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(TestPaper)
admin.site.register(Test)
admin.site.register(TestPaper_Question)
