from django.urls import path

from Task.tasks import views

urlpatterns = [
    path("tasks", views.task_list_view()),
    path("tasks/id", views.task_deatil_view()),
    path("tasks/update/id", views.tasks_update_view()),
    path("tasks/delete/id", views.TaskDeleteView.as_view()),
]
