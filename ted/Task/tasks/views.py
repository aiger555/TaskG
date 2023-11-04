from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from Task.tasks.models import Task



User = get_user_model()

def tasks_list_view(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            tasks = request.user.posts.all()
        else:
            tasks = Task.objects.all()

        return render(request, 'Task/templates/index.html', context = {'tasks': tasks})


def task_detail_view(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'Task/templates/task_detail.html',
                          {'task': task})

def tasks_update_view(request):

    if request.method == 'UPDATE':
        if request.user.is_authenticated:
            tasks = request.user.tasks.all()
            tasks.update()
        else:
            tasks = Task.objects.all()

        return render(request, 'Task/templates/task_update.html', context = {'tasks': tasks})



class TaskCreateView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return ArithmeticError
        return render(request, 'Task/templates/task_create.html', context={'task': tasks_list_view()})


class TaskUpdateView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return ArithmeticError
        return render(request, 'Task/templates/task_create.html', context={'task': task_detail_view()})



class TaskDeleteView(View):
    def __delete__(self, instance):
        task = get_object_or_404(Task, id=id)
        task.delete()
