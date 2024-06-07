from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def Form(request):
    return render(request, 'home.html', {'form': forms.ExampleForm})
