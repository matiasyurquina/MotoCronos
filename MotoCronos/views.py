from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from . import settings
import datetime
from MotoCronos.models import *
 #from datetime import datetime  # Importa datetime
from django.utils import timezone



def home(request):
    cd = datetime.datetime.now()
    #print(cd:"H:i:s")
    return render(request, 'base.html')

#RACERS
def newRacer(request):
    
    return render(request, 'pages/racers/newRacer.html', {'path_racer': True})

def editRacer(request):
    print(request.path)
    return render(request, 'pages/racers/editRacer.html', {'path_racer': True})
    
def ALRacer(request): #alphabetic list 
    print(request.path)
    return render(request, 'pages/racers/ALRacers.html', {'path_racer': True})

def NLRacer(request): #Name or Lastname list 
    print(request.path)
    return render(request, 'pages/racers/NLRacers.html', {'path_racer': True})

def IDRacer(request): #alphabetic list 
    print(request.path)
    return render(request, 'pages/racers/IDracers.html', {'path_racer': True})



#RACES
def newRace(request):

    if request.POST:
        race = Race()
        idRaceMax = Race.objects.count()+1
        race.name = request.POST.get('name')
        race.lapNumber = request.POST.get('laps')
        race.idRace = idRaceMax
        race.date = timezone.now().date()
        race.save()
        return render(request, 'pages/races/newRace.html', {'path_race':True})
    else:
        return render(request, 'pages/races/newRace.html', {'path_race':True})

    

def showAvailableRaces(request):
    races = Race.objects.order_by('name').filter(active='True')
    return render(request, 'pages/races/showAvailableRaces.html', {'path_race':True, 'races': races})


def showPastRaces(request):
    races = Race.objects.order_by('name').filter(active='False')
    # return render(request, 'pages/races/showPastRaces.html', {'path_race':True, 'races': races})

    idRace=request.GET.get('idRace')

    if idRace != None:#I selected an IDRACE
        results = raceResult.objects.filter(idRace=idRace)
        if results:
            print('hola')
        print(results)
        return render(request, 'pages/races/showPastRaces.html', {'path_race':True, 'races': races, 'idRace': idRace, 'results': results})

    return render(request, 'pages/races/showPastRaces.html', {'path_race':True, 'races': races, 'idRace': idRace})

def editRace(request):
    return render(request, 'pages/races/editRace.html', {'path_race':True})



#START RACE
def startRace(request):
    race = Race.objects.order_by('name').filter(active=True)

    return render(request, 'pages/startRace/startRace.html', {'path_startRace':True, 'carreras': race})

def login(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_home') 
        return render(request, 'login.html')
    
    return render(request, 'pages/login.html')


def logout(request):
    logout(request)
    return redirect('login')