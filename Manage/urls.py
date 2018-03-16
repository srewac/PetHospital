from django.urls import path

from . import views

app_name = 'Manage'
urlpatterns = [
    path('manage/', views.index, name='manage'),
    path('forms/', views.forms, name='forms'),
]