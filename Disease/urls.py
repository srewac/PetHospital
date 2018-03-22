from django.urls import path

from . import views
app_name = 'Disease'
urlpatterns = [
    path('select_disease/', views.select_disease, name='select_disease'),
    path('<str:disease_name>/select_subdisease/', views.select_subdisease, name='select_subdisease'),
]