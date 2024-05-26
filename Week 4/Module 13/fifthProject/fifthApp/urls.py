from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="aboutpage"),
    path('form/', views.submitForm, name="submitForm"),
    path('django_form/', views.passwordValidation, name="django_form"),
]
