from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index (request):
    return HttpResponse("Index")
def hello(request, username):
    print(username)
    return HttpResponse("Hello word %s" %username)

def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, id):
   # task = Task.objects.get(id=id)  da una tarea si la encuenta y finaliza
   task = get_object_or_404(Task,id=id)  #muestra 404 más no error
   return HttpResponse("task = %s" %task.title)