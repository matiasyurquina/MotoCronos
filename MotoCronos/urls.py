from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    
    #RACES
    path('race/newRace/', views.newRace, name="newRace"),
    path('race/showAvailableRaces/', views.showAvailableRaces, name="showAvailableRaces"),
    path('race/showPastRaces/', views.showPastRaces, name="showPastRaces"),
    path('race/editRace/', views.editRace, name="editRace"),    

    #RACERS
    path('racer/newRacer/', views.newRacer, name="newRacer"),
    path('racer/ALRacers/', views.ALRacer, name="ALRacers"),
    path('racer/NLRacers/', views.NLRacer, name="NLRacers"),
    path('racer/IDRacers/', views.IDRacer, name="IDRacers"),
    path('racer/editRacer/', views.editRacer, name="editRacer"),
    
    #START RACE
    path('startRace/', views.startRace, name="startRace"),

    path('login/', views.login, name="login"),
    # path('prueba/', views.prueba, name="prueba"),
]
