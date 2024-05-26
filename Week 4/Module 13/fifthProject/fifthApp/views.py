from django.shortcuts import render
from .forms import contactForm, passwordVarificationProject
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    if request.method == 'POST':
        name = request.POST.get('userName')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'about.html')


def submitForm(request):
    return render(request, 'form.html')


def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            #     file = form.cleaned_data['file']
            #     with open('./fifthApp/upload/' + file.name, 'wb+') as destination:
            #         for chunk in file.chunks():
            #             destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, 'django_forms.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'django_forms.html', {'form': form})


def passwordValidation(request):
    if request.method == 'POST':
        form = passwordVarificationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # return render(request, 'django_forms.html', {'form': form})
    else:
        form = passwordVarificationProject()
    return render(request, 'django_forms.html', {'form': form})
