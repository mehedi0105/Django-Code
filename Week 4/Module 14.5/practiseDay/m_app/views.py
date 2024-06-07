from django.shortcuts import render
from .forms import Model_Form
# Create your views here.


# def modelForm(request):
#     if request.method == 'POST':
#         form = Model_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#     else:
#         form = Model_Form()
#     return render(request, 'home.html', {'form': form})

def modelForm(request):
    if request.method == 'POST':
        form = Model_Form(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = Model_Form()
    return render(request, 'home.html', {'form': form})
