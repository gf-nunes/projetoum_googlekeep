from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm


# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios.login")
