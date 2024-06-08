from django.shortcuts import render, redirect
from .forms import CategoryForm
# Create your views here.


def addCategory(request):
    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect('homepage')
    else:
        category = CategoryForm()
    return render(request, 'addCategory.html', {'form': category})
