from django.urls import path
from . import views

app_name = 'polls'



urlpatterns = [
    path('', views.add_room, name='add_room'),
    path('registration_list', views.registration_list, name='registration_list'),
    path('<int:pk>/', views.registration_details, name='registration_details'),
]

