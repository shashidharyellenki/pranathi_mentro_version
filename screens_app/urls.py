from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('course/<int:course_id>', views.course, name="course"),
    path('evalution', views.evalution, name="evalution"),


]