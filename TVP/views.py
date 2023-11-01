from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import TVP as URLTVP
# Create your views here.

def TVP(request): 

     return render(request,"TVP.html",{"TVP",URLTVP.linkk10})