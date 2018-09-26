from django.urls import path
from . import views


urlpatterns = [
    path('', views.Ola_mundo, name='ola_mundo'),
]