from django import views
from django.urls import path
from . import views
from . import forms
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Login
    # path(
    #     "login/",
    #     auth_views.LoginView.as_view(
    #         template_name="login/login.html",
    #         authentication_form=forms.LoginForm,
    #     ),
    #     name="login.login",
    # ),
    path('login/', auth_views.LoginView.as_view(
        template_name='login/login.html'
    ), name='login.login'),
    path("cadastrar/", views.UsuarioCreate.as_view(), name="usuarios.cadastrar"),
    #path('login/', views.validacao, name='login.login'),
    # CRUD
    path('', views.pagina_inicial, name='login.inicial'),
    path('user/<id>/', views.listanotas, name='lista.notas'),
    path('criar/', views.crianotas, name='cria.notas'),
    path('user/<id>/editar/', views.editanotas, name='edita.notas'),
    path('user/<id>/deletar/', views.deletanotas, name='deleta.notas'),
    path('logado/',views.pagina_inicial_logado, name='logado')
]
