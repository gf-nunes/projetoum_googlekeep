from django.shortcuts import get_object_or_404, render
from login.models import Nota, Usuario

# Create your views here.
def listanotas(request, id):
    notas = Nota.objects.filter(usuario_id=id)
    #usuario_nome = Usuario.objects.get()

    id = int(id)
    context={
        'notas':notas,
        'id': id,
    }
    return render(request,'listanotas/lista.html', context)