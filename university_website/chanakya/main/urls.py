from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses_page, name='courses'),
    path('search_student_form/', views.search_student_form, name='search_student_form'),
    path('add_student_form/', views.add_student_form, name='add_student_form'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('search_student/', views.search_student, name='search_student'),
    path('add_student/', views.add_student, name='add_student'),
]

