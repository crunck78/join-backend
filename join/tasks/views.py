from django.http import HttpResponse, JsonResponse

from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


# Create your views here.

@csrf_exempt # for test only
def tasks(request, task_id=None):
    if request.method == 'GET':
        if not task_id == None:
            task = Task.objects.filter(pk=task_id).values().first()
            return JsonResponse(task)
        else:
            tasks = Task.objects.all().values()
            tasksList = list(tasks)
            return JsonResponse(tasksList, safe=False)
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    return HttpResponse("Tasks is working")