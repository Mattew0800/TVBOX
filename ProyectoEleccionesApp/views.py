from django.shortcuts import render, HttpResponse
from .models import C5N, Cronica, Canal10, Canal26, DTV, LN, Telefe, TN, TVP
# Create your views here.

def Inicio(request):
     contador=0
     linkk=""
     for i in (C5N.objects.first()).link:          
          if contador<=23:
               linkk+=i

          contador+=1

          if contador==25:
               linkk+= "embed/"

          if contador>=33 and contador<=43:
               linkk+= i
          
          if contador>43:
               linkk+="?autoplay=1&mute=1"
               break

     contador2=0
     linkk2=""

     for i in (Cronica.objects.first()).link:          
          if contador2<=23:
               linkk2+=i

          contador2+=1

          if contador2==25:
               linkk2+= "embed/"

          if contador2>=33 and contador2<=43:
               linkk2+= i
          
          if contador2>43:
               linkk2+="?autoplay=1&mute=1"
               break
          
     contador3=0
     linkk3=""

     for i in (Canal10.objects.first()).link:          
          if contador3<=23:
               linkk3+=i

          contador3+=1

          if contador3==25:
               linkk3+= "embed/"

          if contador3>=33 and contador3<=43:
               linkk3+= i
          
          if contador3>43:
               linkk3+="?autoplay=1&mute=1"
               break
     

     contador5=0
     linkk5=""

     for i in (Canal26.objects.first()).link:          
          if contador5<=23:
               linkk5+=i

          contador5+=1

          if contador5==25:
               linkk5+= "embed/"

          if contador5>=33 and contador5<=43:
               linkk5+= i
          
          if contador5>43:
               linkk5+="?autoplay=1&mute=1"
               break


     contador6=0
     linkk6=""

     for i in (DTV.objects.first()).link:          
          if contador6<=23:
               linkk6+=i

          contador6+=1

          if contador6==25:
               linkk6+= "embed/"

          if contador6>=33 and contador6<=43:
               linkk6+= i
          
          if contador6>43:
               linkk6+="?autoplay=1&mute=1"
               break

     contador7=0
     linkk7=""

     for i in (LN.objects.first()).link:          
          if contador7<=23:
               linkk7+=i

          contador7+=1

          if contador7==25:
               linkk7+= "embed/"

          if contador7>=33 and contador7<=43:
               linkk7+= i
          
          if contador7>43:
               linkk7+="?autoplay=1&mute=1"
               break

     contador8=0
     linkk8=""

     for i in (Telefe.objects.first()).link:          
          if contador8<=23:
               linkk8+=i

          contador8+=1

          if contador8==25:
               linkk8+= "embed/"

          if contador8>=33 and contador8<=43:
               linkk8+= i
          
          if contador8>43:
               linkk8+="?autoplay=1&mute=1"
               break

     contador9=0
     linkk9=""

     for i in (TN.objects.first()).link:          
          if contador9<=23:
               linkk9+=i

          contador9+=1

          if contador9==25:
               linkk9+= "embed/"

          if contador9>=33 and contador9<=43:
               linkk9+= i
          
          if contador9>43:
               linkk9+="?autoplay=1&mute=1"
               break

     contador10=0
     linkk10=""

     for i in (TVP.objects.first()).link:          
          if contador10<=23:
               linkk10+=i

          contador10+=1

          if contador10==25:
               linkk10+= "embed/"

          if contador10>=33 and contador10<=43:
               linkk10+= i
          
          if contador10>43:
               linkk10+="?autoplay=1&mute=1"
               break




     

     return render(request,"index.html",{'C5N':linkk,'Cronica':linkk2,'Canal10':linkk3,'Canal26':linkk5,'DTV':linkk6,'LN':linkk7,'Telefe':linkk8,'TN':linkk9,'TVP':linkk10})