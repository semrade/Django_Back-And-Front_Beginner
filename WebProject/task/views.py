# Create your views here.
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})


def task_list_json(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return JsonResponse(serializer.data, safe=False)