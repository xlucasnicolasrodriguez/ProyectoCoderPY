from django.shortcuts import render

from AppCoder.models import Persona

# Create your views here.


def mostrar_inicio(request):
    persona = Persona(nombre = 'Lucas', edad = '29', nacimiento = "" )
    contexto = {'persona_1' : persona}    
    return render(request, "AppCoder/inicio.html", contexto)