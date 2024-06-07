
from django.urls import path
from . import views
urlpatterns = [
    path('', views.modelForm, name='modelForm'),
]
