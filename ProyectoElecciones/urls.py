"""
URL configuration for ProyectoElecciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoEleccionesApp import views as Inicioviews
from C5N import views as C5Nviews
from Canal10 import views as Canal10views
from Canal26 import views as Canal26views
from Cronica import views as Cronicaviews
from DTV import views as DTVviews
from LN import views as LNviews
from Telefe import views as Telefeviews
from TN import views as TNviews
from TVP import views as TVPviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicioviews.Inicio, name="Inicio"),
    path('canal10/', Canal10views.Canal10, name="10"),
    path('canal26/', Canal26views.Canal26, name="26"),
    path('c5n/', C5Nviews.C5N, name="C5N"),
    path('cronica/', Cronicaviews.Cronica, name="CTV"),
    path('dtv/', DTVviews.DTV, name="DTV"),
    path('ln/', LNviews.LN, name="LN"),
    path('telefe/', Telefeviews.Telefe, name="TLF"),
    path('tn/', TNviews.TN, name="TN"),
    path('tvp/', TVPviews.TVP, name="TVP"),
]
