from django.db import models
import datetime
# Create your models here.


class Projekt(models.Model):
    Name = models.CharField(max_length=128, null=True)
    Bearbeiter = models.CharField(max_length=128, null=True)


class Requirement(models.Model):
    Name = models.CharField(max_length=128,null=True)
    Beschreibung = models.CharField(max_length=128, default='Bla',null=True)
    Erstellung = models.DateTimeField(null=True, blank=True)
    #Abhängigkeiten
    ProjektID = models.ForeignKey(Projekt, on_delete=models.CASCADE)


class TestCase(models.Model):
    Name = models.CharField(max_length=128,null=True)
    Beschreibung = models.CharField(max_length=128,null=True)
    # Abhängigkeiten
    ProjektID = models.ForeignKey(Projekt, on_delete=models.CASCADE)


class TestRun(models.Model):
    Name = models.CharField(max_length=128, null=True)
    Ergebnis = models.CharField(max_length=128, null=True)
    # Abhängigkeiten
    ProjektID = models.ForeignKey(Projekt, on_delete=models.CASCADE)
    TestCaseID = models.ForeignKey(TestCase, on_delete=models.CASCADE)



