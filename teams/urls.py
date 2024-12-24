from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_team, name='create_team'),
    path('', views.team_list, name='team_list'),
    path('<int:task_id>/assign/', views.assign_task, name='assign_task'),
]
