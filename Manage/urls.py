from django.urls import path

from .views import dashboard, user, test, disease, basic

app_name = 'Manage'
urlpatterns = [
    path('', dashboard.index, name='index'),
    path('user/', user.index, name='user_show'),
    path('disease/', disease.index, name='disease_show'),
    path('test/', test.index, name='test_show'),
]
