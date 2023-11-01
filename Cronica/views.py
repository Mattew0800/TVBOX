from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import Cronica as URLCronica
# Create your views here.

def Cronica(request): 


     return render(request,"CRONICA.html",{"Cronica",URLCronica.linkk2})