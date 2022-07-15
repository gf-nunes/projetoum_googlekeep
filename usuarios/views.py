from django.http import HttpRequest
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm, User, LoginForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse




# Create your views here.

def pagina_inicial(request):
    return render(request, 'login/login.html')

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
    return render (request, 'usuarios/login.html', context)

def pagina_inicial_logado(request, id):
    search = User.objects.get(id=id)
    user_list = User.objects.all()
    new_user = user_list[::-1]
    context = {
        'user': search,
        'new_user': new_user
    }
    return render(request, 'usuarios/login2.html',context)

class UsuarioCreate(CreateView):
    template_name = "usuarios/cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios.login")

# user_list = User.objects.all()