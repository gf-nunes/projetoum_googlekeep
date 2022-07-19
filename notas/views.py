from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm, User, LoginForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Nota, Usuario
from .forms import NotaForm

# Create your views here.

## Página inicial
def pagina_inicial(request):
    return render(request, 'login/login.html')

## Login
def validacao(request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                return HttpResponse('<h1> Seja bem vindo {}', format(user))
            else:
                return HttpResponse ('<h1>senhaaa</h1>')
    form=LoginForm()
    context={
        'form':form,
    }
    return render (request, 'login/login.html', context)

def pagina_inicial_logado(request, id):
    search = Usuario.objects.get(id=id)
    user_list = Usuario.objects.all()
    new_user = user_list[::-1]
    context = {
        'user': search,
        'new_user': new_user[0]
    }
    return render(request, 'login/login2.html',context)

class UsuarioCreate(CreateView):
    template_name = "login/cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("login.login")

# user_list = User.objects.all()

## CRUD
def listanotas(request, id):
    notas = Nota.objects.filter(usuario_id=id)
    autor_id = notas[0].usuario_id
    usuario_nome = Usuario.objects.get(id=autor_id)

    id = int(id)
    context={
        'notas':notas,
        'id': id,
        'usuario_nome': usuario_nome,
    }
    return render(request,'listanotas/lista.html', context)

def crianotas(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario_id = 1 #trocar essa linha para reconhecer o usuario logado
            nota.save()
            return redirect('cria.notas')
    else:
        form = NotaForm()

    return render(request, 'listanotas/nova_nota.html',{'form':form})

def editanotas(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario_id = 1
            nota.save()
            return redirect('lista.notas', id = nota.usuario_id)
    else:
        form = NotaForm(instance=nota)
    return render(request, 'listanotas/edita_nota.html', {'form':form})

def deletanotas(request, id):
    nota = get_object_or_404(Nota,id=id)
    nota.delete()
    return redirect('lista.notas', id=nota.usuario_id)