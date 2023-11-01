from django.shortcuts import render, HttpResponse
from ProyectoEleccionesApp.views import Canal26 as URLCanal26
# Create your views here.

def Canal26(request): 


     return render(request,"Canal26.html",{"Canal26",URLCanal26.linkk5})