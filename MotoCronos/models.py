from datetime import date
from django.db import models

class Racer(models.Model):
    idRacer=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=32, null=False)
    lname=models.CharField(max_length=32, null=False)
    dni=models.PositiveIntegerField(unique=True, null=False)
    birth=models.DateField(null=False)
    cel=models.PositiveIntegerField(blank=True, null=True)
    active=models.BooleanField()
    

class Race(models.Model):
    idRace=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=32, null=False)
    lapNumber=models.SmallIntegerField(null=False)
    date=models.DateField(null=False)
    active=models.BooleanField(default=True)
    
class raceResult(models.Model):
    idStartRace=models.PositiveIntegerField(primary_key=True)
    idRace=models.ForeignKey(Race, on_delete=models.CASCADE, null=False)
    idRacer=models.ForeignKey(Racer, on_delete=models.CASCADE, null=False)
    lap_num=models.PositiveSmallIntegerField()
    lap=models.CharField(8)