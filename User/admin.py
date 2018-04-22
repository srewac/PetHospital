from django.contrib import admin
from .models import User, Usertest, Usertest_question
# Register your models here.

admin.site.register(User)
admin.site.register(Usertest)
admin.site.register(Usertest_question)

