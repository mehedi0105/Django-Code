from django.shortcuts import render

# Create your views here.


def home(request):
    d = {'age': 12, 'country': 'bangladesh', 'course': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 5000
        },
        {
            'id': 2,
            'name': 'Django',
            'fee': 10000
        },
        {
            'id': 3,
            'name': 'C',
            'fee': 1000
        },
    ]}
    return render(request, 'first_app/index.html', d)
