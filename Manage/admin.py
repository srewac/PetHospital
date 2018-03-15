from django.contrib import admin
from .models import People, Medicine, Charge, Analysis, Vaccine, Inhospital

admin.site.register(People)
admin.site.register(Medicine)
admin.site.register(Charge)
admin.site.register(Analysis)
admin.site.register(Vaccine)
admin.site.register(Inhospital)