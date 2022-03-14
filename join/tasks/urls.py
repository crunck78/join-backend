from django.urls import path

from . import views

app_name="tasks"
urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.tasks, name="task")
]