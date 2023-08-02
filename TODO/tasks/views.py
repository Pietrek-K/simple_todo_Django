from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.


def tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')


    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/tasks.html', context)


def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('todo')


    context = {'form':form}
    return render(request, 'tasks/edit-task.html', context)



def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('todo')


    return render(request, 'tasks/delete-task.html')



def completeTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.value = 'finished'
        task.save()
        return redirect('todo')


    return render(request, 'tasks/complete-task.html')

