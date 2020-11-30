from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


#Variablen können auch übergeben werden, hiermit wird die aktuelle Zeit übergeben bei der Erstellung von runserver nicht wenn die Webseite aufgerufen wird
import datetime
now = datetime.datetime.now()

def index(request):
    return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"