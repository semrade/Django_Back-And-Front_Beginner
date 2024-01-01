from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.task_list, name='task_list'),
    path('task-list-json/', views.task_list_json, name='task_list_json'),
]