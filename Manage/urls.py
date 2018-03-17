from django.urls import path

from .views import dashboard, user, test, disease, basic

app_name = 'Manage'
urlpatterns = [
    path('', dashboard.index, name='index'),
    path('user/', user.index, name='user_show'),
    path('user/delete/<int:user_id>', user.user_delete, name='user_delete'),
    path('disease/', disease.index, name='disease_show'),
    path('test/test', test.test_index, name='test_show'),
    path('test/testpaper', test.testpapaer_index, name='testpaper_show')
]
