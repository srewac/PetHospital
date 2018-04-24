from django.urls import path

from . import views

app_name = 'Disease'
urlpatterns = [
    path('select_disease/', views.select_disease, name='select_disease'),
    path('<str:disease_name>/select_subdisease/', views.select_subdisease, name='select_subdisease'),
    path('subdisease_desc/<int:subdisease_id>', views.subdisease_desc, name='subdisease_desc'),
    path('disease_example/<int:disease_example_id>', views.disease_example_desc, name='disease_example_desc'),
]
