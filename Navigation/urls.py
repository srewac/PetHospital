from django.urls import path

from . import views

app_name = 'Navigation'
urlpatterns = [
    path('hall/', views.hall, name='hall'),
    path('ward/', views.ward, name='ward'),
]