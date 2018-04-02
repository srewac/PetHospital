from django.urls import path
from . import views

app_name = 'Test'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('select_disease/', views.select_disease, name='select_disease'),
    path('<str:disease_name>/select_paper/', views.select_paper, name='select_paper'),
    path('selected_paper/', views.selected_paper, name='selected_paper'),
    path('paper/', views.paper, name='paper'),
    path('result/', views.result, name='result'),
    path('result_detail/<int:test_id>/', views.result_detail, name='result_detail'),
]