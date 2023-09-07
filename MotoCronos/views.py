from django.shortcuts import render
from . import settings

def home(request):
    return render(request, 'home.html')

def createRacer(request):
    return render(request, 'racer/index.html')

def createRace(request):
    return render(request, 'race/index.html')

def startRace(request):
    return render(request, 'startRace/index.html')