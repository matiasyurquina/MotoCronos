from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
import datetime
from MotoCronos.models import *
from django.utils import timezone
from django.db.models import Q


############################################################# ONLY FUNCTIONS #############################################################
def getPersonByDNI(dni):

    try:
        person = Racer.objects.get(dni=dni)
    except:
        return None

    return person

def getPersonByID(idRacer):

    try:
        person = Racer.objects.get(pk=idRacer)
    except:
        return None

    return person

def getRacerByName(name):
    racers = Racer.objects.filter(Q(name__icontains=name) | Q(lname__icontains=name))

    if racers:
        return racers
    else:
        return None
    
def saveReg(object):
    try:
        object.save()
        return 0
    except IntegrityError:
        return 1
    except:
        return 2 

def editRacerFunction(racer:Racer, request):
    racer.name = request.POST.get('name').strip(' ').upper()
    racer.lname = request.POST.get('lname').strip(' ').upper()
    racer.dni = request.POST.get('dni').strip(' ')
    racer.cel = request.POST.get('cel').strip(' ')
    racer.birth = request.POST.get('birth')
    racer.active = request.POST.get('active')
    # print(racer)
    return saveReg(racer)
    

############################################################# ONLY VIEWS #############################################################
def home(request):
    cd = datetime.datetime.now()
    return render(request, 'base.html')

#RACERS
def newRacer(request):

    if request.POST:#submit
        racer = Racer()
        racer.idRacer = Racer.objects.count()+1
        racer.name = request.POST.get('name').strip(' ').upper()
        racer.lname = request.POST.get('lname').strip(' ').upper()
        racer.dni = request.POST.get('dni').strip(' ')
        racer.dni = racer.dni.strip(' ')
        racer.birth = request.POST.get('birth')
        racer.cel = request.POST.get('cel')
        racer.active = True
        racer.save()
        return render(request, 'pages/racers/newRacer.html', {'path_racer': True})
    else: 
        return render(request, 'pages/racers/newRacer.html', {'path_racer': True})

def editRacer(request):

    idRacer = request.GET.get('idRacer')
    racer = getPersonByID(idRacer)

    if request.POST.get('update') != None:#if UPDATE button was pressed
        res = editRacerFunction(racer, request)
        racer = getPersonByID(idRacer)

        if res == 0:#success
            return render(request, 'pages/racers/editRacer.html', {'path_racer': True, 'racer': racer, 'msg': 'Datos guardados'})
        elif res == 1:#IntegrityError
            return render(request, 'pages/racers/editRacer.html', {'path_racer': True, 'racer': racer, 'error': f"El corredor con DNI {racer.dni} ya existe"})
        else:#UnknownError
            return render(request, 'pages/racers/editRacer.html', {'path_racer': True, 'racer': racer, 'error':'Ocurrió un error inesperado'})
    
    if racer == None:
        return render(request, 'pages/racers/editRacer.html', {'path_racer': True})
    else:
        return render(request, 'pages/racers/editRacer.html', {'path_racer': True, 'racer': racer})
    
def ALRacer(request): #alphabetic listing
    racers = Racer.objects.all().order_by('lname', 'name', 'dni')
    return render(request, 'pages/racers/ALRacers.html', {'path_racer': True, 'racers': racers})

def NLRacer(request): #Name or Lastname listing 

    if request.POST:#sumbit
        racers = getRacerByName(request.POST.get('name'))
        if racers == None:
            error = 'No se encontraron resultados'
            
            return render(request, 'pages/racers/NLRacers.html', {'path_racer': True, 'racers': racers, 'error': error})
        else:
            return render(request, 'pages/racers/NLRacers.html', {'path_racer': True, 'racers': racers})
    else:#INDEX    
        return render(request, 'pages/racers/NLRacers.html', {'path_racer': True})

def IDRacer(request): #DNI listing 
    
    if request.POST:#submit
        racer = getPersonByDNI(request.POST.get('dni'))
        if racer == None:
            error = 'No se encontraron resultados'
            return render(request, 'pages/racers/IDracers.html', {'path_racer': True, 'racer': racer, 'error': error})
        else:
            return render(request, 'pages/racers/IDracers.html', {'path_racer': True, 'racer': racer})
    else:#index
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
        reg = saveReg(race)
        if reg == 0: #Success
            return render(request, 'pages/races/newRace.html', {'path_race':True})
        elif reg == 1:#Itegrity error
            return render(request, 'pages/races/newRace.html', {'path_race':True})
        else:#Some Error
            return render(request, 'pages/races/newRace.html', {'path_race':True})
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
        return render(request, 'pages/races/showPastRaces.html', {'path_race':True, 'races': races, 'idRace': idRace, 'results': results})

    return render(request, 'pages/races/showPastRaces.html', {'path_race':True, 'races': races, 'idRace': idRace})

def editRace(request):
    return render(request, 'pages/races/editRace.html', {'path_race':True})



#START RACE
def startRace(request):
    race = Race.objects.order_by('name').filter(active=True)
    idRace = request.GET.get('idRace')
    racersList=None
    if request.POST:
        racersList=request.POST.getlist('racersList')
    
    if racersList!=None:
        racers = Racer.objects.order_by('lname', 'name', 'dni').filter(idRacer__in=racersList,   active=True)
        return render(request, 'pages/startRace/startRace.html', {'path_startRace':True, 'racers': racers, 'idRace': idRace, 'race': race, 'racersList': racersList})


    if idRace != None:
        racers = Racer.objects.order_by('lname', 'name', 'dni').filter(active=True)
        race = Race.objects.get(pk=idRace)
        return render(request, 'pages/startRace/startRace.html', {'path_startRace':True, 'racers': racers, 'idRace': idRace, 'race': race})
    else:
        return render(request, 'pages/startRace/startRace.html', {'path_startRace':True, 'races': race})

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

def prueba(request):
    return render(request, 'prueba.html')