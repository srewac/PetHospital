from django.urls import path

from . import views

app_name = 'Navigation'
urlpatterns = [
    path('hall/', views.hall, name='hall'),
    path('TwoD_Navigation', views.TwoD_Navigation, name='TwoD_Navigation'),
    path('TwoD_getRooms/<int:room_id>', views.TwoD_getRooms, name='TwoD_getRooms'),
    path('ward/', views.ward, name='ward'),
]
