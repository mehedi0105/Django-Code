from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from sixthApp.forms import StudentForm


def home(request):
    student = models.Student.objects.all()
    return render(request, "sixthApp/home.html", {'student': student})


def delete(request, roll):
    std = models.Student.objects.get(pk=roll).delete()
    print(std)
    return redirect("home")


def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, "sixthApp/home.html", {'forms': form})
