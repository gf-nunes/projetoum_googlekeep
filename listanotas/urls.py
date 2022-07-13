from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('user/<id>/', views.listanotas, name='lista.notas'),
    path('criar/', views.crianotas, name='cria.notas'),
    path('user/<id>/editar/', views.editanotas, name='edita.notas'),
    path('user/<id>/deletar/', views.deletanotas, name='deleta.notas'),
]
