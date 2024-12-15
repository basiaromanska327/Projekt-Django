from django.db import models
from management.models import User

class Film(models.Model):
    nazwa = models.CharField(verbose_name="Tytul filmu", max_length=64)
    plakat = models.ImageField(verbose_name="Plakat")

    class Meta:
        verbose_name_plural = "Filmy"

    def __str__(self):
        return f"Film {self.nazwa}"    

class Sala(models.Model):
    nazwa = models.CharField(verbose_name="Nazwa sali", max_length=32)
    liczba_miejsc = models.IntegerField(verbose_name="Liczba miejsc")

    class Meta:
        verbose_name_plural = "Sale"

    def __str__(self):
        return f"Sala {self.nazwa}"
    
class Seans(models.Model):
    film = models.ForeignKey(Film, on_delete=models.PROTECT)
    termin = models.DateTimeField(verbose_name="Termin")
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Seanse"

    def __str__(self):
        return f"Seans {self.film.nazwa} {self.termin.strftime("%Y-%m-%d %H:%M")} Sala {self.sala.nazwa}"
    