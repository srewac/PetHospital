from django.urls import path

from .views import dashboard, user, test, disease
from .views.basic import room

app_name = 'Manage'
urlpatterns = [
    path('', dashboard.index, name='index'),
    # user urls
    path('user/', user.index, name='user_show'),
    path('user/user_dict', user.user_dict, name='user_dict'),
    path('user/delete/<int:user_id>', user.user_delete, name='user_delete'),
    path('user/update/', user.user_update, name='user_update'),
    path('user/create', user.user_create, name='user_create'),
    # disease urls
    path('disease_example', disease.disease_example, name='disease_example_show'),
    path('disease_example_dict', disease.disease_example_dict, name='disease_example_dict'),
    path('disease_example_create', disease.disease_example_create, name='disease_example_create'),
    # test urls
    path('test/test', test.test_index, name='test_show'),
    path('test/testpaper', test.testpapaer_index, name='testpaper_show'),
    path('test/question', test.question_index, name='question_show'),
    path('test/sub_disease_dict/<int:disease_id>', test.sub_disease_dict, name='sub_disease_dict'),
    path('test/question_dict', test.question_dict, name='question_dict'),
    path('test/question_create', test.question_create, name='question_create'),
    path('test/question_create_dict', test.question_create_dict, name='question_create_dict'),
    path('test/question_modify', test.question_modify, name='question_modify'),
    path('test/question_modify_dict/<int:question_id>', test.question_modify_dict, name='question_modify_dict'),
    path('test/question_delete/<int:question_id>', test.question_delete, name='question_delete'),

    # basic urls
    path('basic/room', room.room, name='room'),
    path('basic/room_dict', room.room_dict, name='room_dict'),
    path('basic/room_modify', room.room_modify, name='room_modify'),
    path('basic/room_create', room.room_create, name='room_create'),
    path('basic/room_delete/<int:room_id>', room.room_delete, name='room_delete'),
]
