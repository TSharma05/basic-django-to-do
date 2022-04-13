from django.shortcuts import render, redirect
from .form import ItemForm
from .models import Item

# Create your views here.

def all_tasks(request):
    tasks = Item.objects.all()
    context = {
        "tasks" : tasks
    }
    return render(request, "items/tasks.html", context)

def index(request):
    if request.method == "GET":
        form = ItemForm()
        context = {
            "form" : form
        }
        return render(request, "items/index.html", context)
    
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items:all_tasks')
    
def task_view(request, task_id):
    task = Item.objects.get(id=task_id)
    context = {
        'task' :task
    }
    return render(request, 'items/details.html', context)

def task_update(request, task_id):
    task = Item.objects.get(id=task_id)
    form = ItemForm(request.POST or None, instance=task)
    data = {
        'form' : form,
        'new_or_edit' : 'Edit',
    }
    if form.is_valid():
        form.save()
        return redirect('items:all_tasks')
    return render(request, 'items/index.html', data)

def task_delete(request, task_id):
    task = Item.objects.get(id=task_id)
    context = {
        'task' : task
    }
    if request.method == 'POST':
        task.delete()
        return redirect('items:all_tasks')
    return render(request, 'items/delete.html', context)