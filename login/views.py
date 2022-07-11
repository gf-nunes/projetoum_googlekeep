from django.http import HttpRequest
from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'login/login.html')
