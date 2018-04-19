from django.urls import path
from .views import dashboard, user, test, disease
from .views.basic import people, room, analysis, vaccine, inhospital, medicine, charge

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
    path('disease_example_create_dict', disease.disease_example_create_dict, name='disease_example_create_dict'),
    path('disease_example_create', disease.disease_example_create, name='disease_example_create'),
    path('process_create', disease.process_create, name='process_create'),
    path('disease_example_detail/<int:disease_example_id>', disease.disease_example_detail,
         name='disease_example_detail'),
    path('disease_example_detail_dict/<int:disease_example_id>', disease.disease_example_detail_dict,
         name='disease_example_detail_dict'),
    path('process_delete/<int:process_id>', disease.process_delete, name='process_delete'),
    path('disease_example_delete/<int:disease_example_id>', disease.disease_example_delete,
         name='disease_example_delete'),
    path('disease_example_modify_dict/<int:disease_example_id>', disease.disease_example_modify_dict,
         name='disease_example_modify_dict'),
    path('disease_example_modify',disease.disease_example_modify,name='disease_example_modify'),
    # test urls
    path('test/sub_disease_dict/<int:disease_id>', test.sub_disease_dict, name='sub_disease_dict'),
    path('test/question', test.question_index, name='question_show'),
    path('test/question_dict', test.question_dict, name='question_dict'),
    path('test/question_create', test.question_create, name='question_create'),
    path('test/disease_sub_disease_dict', test.disease_sub_disease_dict, name='disease_sub_disease_dict'),
    path('test/question_modify', test.question_modify, name='question_modify'),
    path('test/question_modify_dict/<int:question_id>', test.question_modify_dict, name='question_modify_dict'),
    path('test/question_delete/<int:question_id>', test.question_delete, name='question_delete'),
    # testpaper urls
    path('test/testpaper', test.testpaper_index, name='testpaper_show'),
    path('test/testpaper_dict', test.testpaper_dict, name='testpaper_dict'),
    path('test/testpaper_delete/<int:testpaper_id>', test.testpaper_delete, name='testpaper_delete'),
    path('test/testpaper_create_show', test.testpaper_create_show, name='testpaper_create_show'),
    path('test/testpaper_create', test.testpaper_create, name='testpaper_create'),
    path('test/testpaper_modify_dict/<int:testpaper_id>', test.testpaper_modify_dict, name='testpaper_modify_dict'),
    path('test/testpaper_modify', test.testpaper_modify, name='testpaper_modify'),
    path('test/select_question/<int:testpaper_id>', test.select_question, name='select_question'),
    path('test/select_question_dict/<int:testpaper_id>', test.select_question_dict, name='select_question_dict'),
    path('test/testpaper_question_add/<int:testpaper_id>/<int:question_id>', test.testpaper_question_add,
         name='testpaper_question_add'),
    path('test/testpaper_question_delete/<int:testpaper_id>/<int:question_id>', test.testpaper_question_delete,
         name='testpaper_question_delete'),
    path('test/testpaper_question_delete_all/<int:testpaper_id>', test.testpaper_question_delete_all,
         name='testpaper_question_delete_all'),
    # test urls
    path('test/test', test.test_index, name='test_show'),
    path('test/test_dict', test.test_dict, name='test_dict'),
    path('test/test_create', test.test_create, name='test_create'),
    path('test/test_modify_dict/<int:test_id>', test.test_modify_dict, name='test_modify_dict'),
    path('test/test_modify/<int:test_id>', test.test_modify, name='test_modify'),
    path('test/test_delete/<int:test_id>', test.test_delete, name='test_delete'),
    path('test/test_detail_show/<int:test_id>', test.test_detail_show, name='test_detail_show'),
    path('test/test_detail_dict/<int:test_id>', test.test_detail_dict, name='test_detail_dict'),
    path('test/test_detail_add_user/<int:test_id>/<int:user_id>', test.test_detail_add_user,
         name='test_detail_add_user'),
    path('test/test_detail_delete_user/<int:test_id>/<int:user_id>', test.test_detail_delete_user,
         name='test_detail_delete_user'),
    path('test/test_detail_add_all_user/<int:test_id>', test.test_detail_add_all_user,
         name='test_detail_add_all_user'),
    path('test/test_detail_delete_all_user/<int:test_id>', test.test_detail_delete_all_user,
         name='test_detail_delete_all_user'),
    # room urls
    path('basic/room', room.room, name='room'),
    path('basic/room_dict', room.room_dict, name='room_dict'),
    path('basic/room_modify', room.room_modify, name='room_modify'),
    path('basic/room_create', room.room_create, name='room_create'),
    path('basic/room_delete/<int:room_id>', room.room_delete, name='room_delete'),
    # people urls
    path('basic/people', people.people, name="people_show"),
    path('basic/people/people_dict', people.people_dict, name='people_dict'),
    path('basic/people/delete/<int:people_id>', people.people_delete, name='people_delete'),
    path('basic/people/update', people.people_update, name='people_update'),
    path('basic/people/create', people.people_create, name='people_create'),
    # medicine urls
    path('basic/medicine', medicine.medicine, name="medicine_show"),
    path('basic/medicine/medicine_dict', medicine.medicine_dict, name='medicine_dict'),
    path('basic/medicine/delete/<int:medicine_id>', medicine.medicine_delete, name='medicine_delete'),
    path('basic/medicine/update', medicine.medicine_update, name='medicine_update'),
    path('basic/medicine/create', medicine.medicine_create, name='medicine_create'),
    # charge urls
    path('basic/charge', charge.charge, name="charge_show"),
    path('basic/charge/charge_dict', charge.charge_dict, name='charge_dict'),
    path('basic/charge/delete/<int:charge_id>', charge.charge_delete, name='charge_delete'),
    path('basic/charge/modify_charge_init/<int:people_id>', charge.modify_charge_init, name='modify_charge_init'),
    path('basic/charge/modify_charge_room_select', charge.modify_charge_room_select, name='modify_charge_room_select'),
    path('basic/charge/update', charge.charge_update, name='charge_update'),
    path('basic/charge/create_charge_room_select', charge.create_charge_room_select, name='create_charge_room_select'),
    path('basic/charge/create', charge.charge_create, name='charge_create'),
    # room urls
    path('basic/room', room.room, name='room_show'),
    path('basic/room_dict', room.room_dict, name='room_dict'),
    path('basic/room_modify_dict/<int:room_id>', room.room_modify_dict,name='room_modify_dict'),
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
