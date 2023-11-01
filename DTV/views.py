from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import DTV as URLDTV
# Create your views here.

def DTV(request): 


     return render(request,"DTV.html",{"DTV",URLDTV.linkk6})