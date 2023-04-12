from asyncio import tasks
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def HomePage(request):

    forms = TaskForm()

    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')
    context = {
        'tasks': Tasks.objects.all(),
        'forms': forms
    }
    return render(request, 'task/home.html', context)

def updateTask(request, pk):
    tasks = Tasks.objects.get(id=pk)

    forms = TaskForm(instance=tasks)
    if request.method == 'POST':
        forms = TaskForm(request.POST, instance=tasks)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    context = {
            'forms': forms
        }
    return render(request,'task/update_task.html', context)

def deleteTask(request, pk):
    items = Tasks.objects.get(id=pk)

    if request.method == "POST":
        items.delete()
        return redirect('/')

    context = {'items': items}
    return render(request, 'task/comfirm_task_delete.html', context)