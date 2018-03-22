from django.urls import path

from . import views
app_name = 'Test'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('select_disease/', views.select_disease, name='select_disease'),
    path('<str:disease>/select_paper/', views.select_paper, name='select_paper'),
    path('test_management/', views.test_management, name='test_management'),
]