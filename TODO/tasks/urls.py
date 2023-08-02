from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.tasks, name='todo'),
    path('edit-task/<str:pk>/', views.editTask, name="edit-task"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
    path('complete-task/<str:pk>/', views.completeTask, name="complete-task"),
]
