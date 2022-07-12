from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('user/<id>/', views.listanotas, name='lista.notas'),
]
