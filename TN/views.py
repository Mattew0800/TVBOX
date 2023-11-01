from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import TN as URLTN
# Create your views here.

def TN(request): 


     return render(request,"TN.html",{"TN",URLTN.linkk9})