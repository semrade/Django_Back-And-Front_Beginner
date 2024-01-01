from django.urls import path
from .views import experience_list, experience_list_json, education_list_json
from . import views

urlpatterns = [
    path('education-list/', views.education_list, name='education_list'),
    path('experience-list/', views.experience_list, name='experience_list'),
    path('experience-list-json/', experience_list_json, name='experience-list-json'),
    path('education-list-json/', education_list_json, name='education-list-json'),
]
