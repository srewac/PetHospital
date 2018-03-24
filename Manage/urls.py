from django.urls import path

from .views import dashboard, user, test, disease

from .views.basic import people,room


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
    path('test/sub_disease_dict/<int:disease_id>', test.sub_disease_dict, name='sub_disease_dict'),
    path('test/test', test.test_index, name='test_show'),
    path('test/question', test.question_index, name='question_show'),
    path('test/question_dict', test.question_dict, name='question_dict'),
    path('test/question_create', test.question_create, name='question_create'),
    path('test/disease_sub_disease_dict', test.disease_sub_disease_dict, name='disease_sub_disease_dict'),
    path('test/question_modify', test.question_modify, name='question_modify'),
    path('test/question_modify_dict/<int:question_id>', test.question_modify_dict, name='question_modify_dict'),
    path('test/question_delete/<int:question_id>', test.question_delete, name='question_delete'),
    path('test/testpaper', test.testpaper_index, name='testpaper_show'),
    path('test/testpaper_dict', test.testpaper_dict, name='testpaper_dict'),
    path('test/testpaper_delete/<int:testpaper_id>', test.testpaper_delete, name='testpaper_delete'),
    path('test/testpaper_create_show', test.testpaper_create_show, name='testpaper_create_show'),
    path('test/testpaper_create', test.testpaper_create, name='testpaper_create'),
    path('test/testpaper_modify_dict/<int:testpaper_id>', test.testpaper_modify_dict, name='testpaper_modify_dict'),
    path('test/testpaper_modify', test.testpaper_modify, name='testpaper_modify'),
    path('test/select_question/<int:testpaper_id>', test.select_question, name='select_question'),
    path('test/select_question_dict/<int:testpaper_id>', test.select_question_dict, name='select_question_dict'),
    path('test/testpaper_question_add/<int:testpaper_id>/<int:question_id>', test.testpaper_question_add, name='testpaper_question_add'),
    path('test/testpaper_question_delete/<int:testpaper_id>/<int:question_id>', test.testpaper_question_delete,
         name='testpaper_question_delete'),
    path('test/testpaper_question_delete_all/<int:testpaper_id>', test.testpaper_question_delete_all, name='testpaper_question_delete_all'),
    # people urls
    path('basic/people', people.people, name="people_show"),
    path('basic/people/people_dict', people.people_dict, name='people_dict'),
    path('basic/people/delete/<int:people_id>', people.people_delete, name='people_delete'),
    path('basic/people/update', people.people_update, name='people_update'),
    path('basic/people/create', people.people_create, name='people_create'),
    # room urls
    path('basic/room', room.room, name='room'),
    path('basic/room_dict', room.room_dict, name='room_dict'),
    path('basic/room_modify', room.room_modify, name='room_modify'),
    path('basic/room_create', room.room_create, name='room_create'),
    path('basic/room_delete/<int:room_id>', room.room_delete, name='room_delete'),

]
