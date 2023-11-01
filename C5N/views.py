from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import C5N as URLC5N
# Create your views here.

def C5N(request): 


     return render(request,"C5N.html",{"C5N",URLC5N.linkk})