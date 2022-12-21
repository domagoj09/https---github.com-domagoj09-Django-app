from django.db import models
from django.utils import timezone

# Create your models here.


class Profesor(models.Model): #supervisor natjecanja
    prof_ime = models.CharField(max_length=30)
    prof_prezime = models.CharField(max_length=30)
    prof_email = models.EmailField()

    def __str__(self):
        return self.prof_email        


class Natjecanje(models.Model):
    natjecanje_naslov = models.CharField(max_length=100)
    natjecanje_opis = models.TextField()
    natjecanje_vrijeme = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.natjecanje_naslov


class Sudionik(models.Model):
    sudionik_ime = models.CharField(max_length=25)
    sudionik_prezime = models.CharField(max_length=50)
    student_broj_xice = models.CharField(max_length=10)
    student_natjecanja = models.ManyToManyField(Natjecanje)        

    def __str__(self):
        return self.sudionik_prezime, self.sudionik_ime      



