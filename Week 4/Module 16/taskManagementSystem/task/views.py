from django.shortcuts import render, redirect
from . import models
from . import forms
from task.forms import TaskForm
# Create your views here


def addTask(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('homepage')
    else:
        task = TaskForm()
    return render(request, 'addTask.html', {'form': task})


def edit_post(request, id):
    post = models.Task.objects.get(pk=id)
    Post_form = forms.TaskForm(instance=post)
    if request.method == 'POST':
        Post_form = forms.TaskForm(request.POST, instance=post)
        if Post_form.is_valid():
            Post_form.save()
            return redirect('homepage')
    return render(request, 'addTask.html', {'form': Post_form})


def delete_post(request, id):
    post = models.Task.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
