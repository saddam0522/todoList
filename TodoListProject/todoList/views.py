
from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm()
    return render(request, 'home.html', {'form': form})

def show_task(request):
    tasklist = TaskModel.objects.filter(is_completed=False)      
    return render(request,'show_task.html', {'task': tasklist})


def edit_task(request , id):
    todo = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = todo)
    if request.method == 'POST':
        info = TaskForm(request.POST,instance = todo)
        if info.is_valid():
            info.save()
            print(info.cleaned_data)
            return redirect('show_task')
    else:
        todo= TaskForm()
    return render(request,'edit_task.html',{'form':form})

def delete_task(request,id):
    todo = TaskModel.objects.get(pk = id).delete()
    return redirect('show_task')

def complete_task(request,id):
    task = TaskModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    tasklist = TaskModel.objects.filter(is_completed=True)      
    return render(request,'completed_task.html', {'task': tasklist})

def completed_tasks(request):
    
    tasklist = TaskModel.objects.filter(is_completed=True)      
    return render(request,'completed_task.html', {'task': tasklist})
