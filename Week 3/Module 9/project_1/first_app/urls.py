from django.urls import path
from .views import courses, about, home
urlpatterns = [
    path('courses/', courses),
    path('', home),
    path('about/', about),
]
