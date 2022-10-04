from django.shortcuts import render, HttpResponse
from django.template import loader
from AppCoder.models import Familiar

# Create your views here.
def familia (self):
    familiar1 = Familiar( nombre = "Lara",  edad = 27, nacimiento = "1995-08-03" )
    familiar1.save()

    familiar2 = Familiar( nombre = "Camilo", edad = 10, nacimiento = "2012-06-28" )
    familiar2.save()

    familiar3 = Familiar( nombre = "Lucas", edad = 29, nacimiento = "1993-06-02" )
    familiar3.save()

    plantilla = loader.get_template('inicio.html')
    familiares = {'familiares' : [familiar1, familiar2, familiar3]}
    documento = plantilla.render(familiares)
    return HttpResponse(documento)
