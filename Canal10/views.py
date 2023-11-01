from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import Canal10 as URLCanal10
# Create your views here.

def Canal10(request): 


     return render(request,"Canal10.html",{"Canal10",URLCanal10.linkk3})