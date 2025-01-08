from django.urls import path

from task.api import views

urlpatterns = [
    path('tasks/', views.TasksList.as_view()),
]