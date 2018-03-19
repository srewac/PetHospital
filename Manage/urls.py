from django.urls import path

from .views import dashboard, user, test, disease, basic

app_name = 'Manage'
urlpatterns = [
    path('', dashboard.index, name='index'),
    path('user/', user.index, name='user_show'),
    path('user/user_dict', user.user_dict, name='user_dict'),
    path('user/delete/<int:user_id>', user.user_delete, name='user_delete'),
    path('user/update/', user.user_update, name='user_update'),
    path('user/create', user.user_create, name='user_create'),
    # path('disease/', disease.index, name='disease_show'),
    path('disease_example', disease.disease_example, name='disease_example_show'),
    path('disease_example_dict', disease.disease_example_dict, name='disease_example_dict'),
    path('test/test', test.test_index, name='test_show'),
    path('test/testpaper', test.testpapaer_index, name='testpaper_show')
]
