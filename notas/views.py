from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Nota, User
from .forms import UsuarioForm, LoginForm, NotaForm


# Create your views here.

## Página inicial
def pagina_inicial(request):
    return render(request, 'login/login.html')

## Login
def validacao(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"Bem vindo, {username}")
                usuario_id = request.user.id
                return redirect('lista.notas', id=usuario_id)
            else:
                messages.error(request, "Senha ou usuário inválidos.")
        else:
            messages.error(request, "Senha ou usuário inválidos.")
    form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'listanotas/lista.html', context)

def pagina_inicial_logado(request):
    #search = User.objects.get(id=id)
    user_list = User.objects.all()
    new_user = user_list[::-1]
    nome_user_logado = request.user
    id_user_logado = request.user.id
    context = {
        'new_user': new_user[0],
        'nome': nome_user_logado,
        'id':id_user_logado,
    }
    return render(request, 'login/usuario_logado.html',context)

class UsuarioCreate(CreateView):
    template_name = "login/cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("login.login")

# user_list = User.objects.all()

## CRUD
def listanotas(request, id):
    user = request.user.id
    notas = Nota.objects.filter(usuario_id=user)
    autor_id = notas[0].usuario_id
    usuario_nome = User.objects.get(id=autor_id)

    id = int(id)
    context={
        'notas':notas,
        'id': id,
        'usuario_nome': usuario_nome,
        'user':user,
    }
    return render(request,'listanotas/lista.html', context)

def crianotas(request):
    user = request.user.id
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario_id = user
            nota.save()
            return redirect('lista.notas', id = user)
    else:
        form = NotaForm()

    return render(request, 'listanotas/nova_nota.html',{'form':form})

def editanotas(request, id):
    user = request.user.id
    nota = get_object_or_404(Nota, id=id)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario_id = user
            nota.save()
            return redirect('lista.notas', id = nota.usuario_id)
    else:
        form = NotaForm(instance=nota)
    return render(request, 'listanotas/edita_nota.html', {'form':form})

def deletanotas(request, id):
    nota = get_object_or_404(Nota,id=id)
    nota.delete()
    return redirect('lista.notas', id=nota.usuario_id)