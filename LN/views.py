from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import LN as URLLN
# Create your views here.

def LN(request): 


     return render(request,"LN.html",{"LN",URLLN.linkk7})