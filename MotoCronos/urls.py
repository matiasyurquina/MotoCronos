from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('newRace/', views.createRace, name="newRace"),
    path('newRacer/', views.createRacer, name="newRacer"),
    path('startRace/', views.startRace, name="startRace"),
]
