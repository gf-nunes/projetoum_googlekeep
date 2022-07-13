from django.shortcuts import get_object_or_404, redirect, render
from login.models import Nota, Usuario
from .forms import NotaForm

# Create your views here.
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
            nota.usuario_id = 2 #trocar essa linha para reconhecer o usuario logado
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
            nota.usuario_id = 2
            nota.save()
            return redirect('lista.notas', id = nota.usuario_id)
    else:
        form = NotaForm(instance=nota)
    return render(request, 'listanotas/edita_nota.html', {'form':form})

def deletanotas(request, id):
    nota = get_object_or_404(Nota,id=id)
    nota.delete()
    return redirect('lista.notas', id=nota.usuario_id)