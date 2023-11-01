from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import Telefe as URLTelefe
# Create your views here.

def Telefe(request): 


     return render(request,"Telefe.html",{"Telefe",URLTelefe.linkk8})