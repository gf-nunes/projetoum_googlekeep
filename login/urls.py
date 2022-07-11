from django import views
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    
    path('', views.pagina_inicial, name='login.inicial'),
]
