from django.urls import path

from .views import dashboard, user, test, disease

from .views.basic import people, room, analysis, vaccine, inhospital


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

    # people urls
    path('basic/people', people.people, name="people_show"),
    path('basic/people/people_dict', people.people_dict, name='people_dict'),
    path('basic/people/delete/<int:people_id>', people.people_delete, name='people_delete'),
    path('basic/people/update', people.people_update, name='people_update'),
    path('basic/people/create', people.people_create, name='people_create'),

    # room urls
    path('basic/room', room.room, name='room_show'),
    path('basic/room_dict', room.room_dict, name='room_dict'),
    path('basic/room_modify', room.room_modify, name='room_modify'),
    path('basic/room_create', room.room_create, name='room_create'),
    path('basic/room_delete/<int:room_id>', room.room_delete, name='room_delete'),

    # analysis urls
    path('basic/analysis', analysis.analysis, name='analysis_show'),
    path('basic/analysis_dict', analysis.analysis_dict, name='analysis_dict'),
    path('basic/analysis_create', analysis.analysis_create, name='analysis_create'),
    path('basic/analysis_delete/<int:analysis_id>', analysis.analysis_delete, name='analysis_delete'),

    # vaccine urls
    path('basic/vaccine', vaccine.vaccine, name='vaccine_show'),
    path('basic/vaccine_dict', vaccine.vaccine_dict, name='vaccine_dict'),
    path('basic/vaccine_modify', vaccine.vaccine_modify, name='vaccine_modify'),
    path('basic/vaccine_create', vaccine.vaccine_create, name='vaccine_create'),
    path('basic/vaccine_delete/<int:vaccine_id>', vaccine.vaccine_delete, name='vaccine_delete'),

    # inhospital urls
    path('basic/inhospital', inhospital.inhospital, name='inhospital_show'),
    path('basic/inhospital_dict', inhospital.inhospital_dict, name='inhospital_dict'),
    path('basic/inhospital_modify_dict/<int:id>', inhospital.inhospital_modify_dict, name='inhospital_modify_dict'),
    path('basic/inhospital_modify', inhospital.inhospital_modify, name='inhospital_modify'),
    path('basic/inhospital_create_dict', inhospital.inhospital_create_dict, name='inhospital_create_dict'),
    path('basic/inhospital_create', inhospital.inhospital_create, name='inhospital_create'),
    path('basic/inhospital_delete/<int:patient_id>', inhospital.inhospital_delete, name='inhospital_delete'),
]
