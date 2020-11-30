from django.db import models
import datetime
# Create your models here.
import uuid  # Für den Primary Key
from django.db.models import F
from django.urls import reverse
from django.contrib.auth.models import User

#import der Choices damit die überall verwendbar sind
from .choices import *



class Professor(models.Model):
    Professorennummer = models.AutoField(primary_key=True, null=False, unique=True)
    Name = models.CharField(max_length=128, null=True, help_text='Name des Professors')
    Passwort = models.CharField(max_length=128, null=True)

#als erste Idee, um die Sachen zu identifizieren zu können
    def __str__(self):
        ret = str(self.Name) + str(" ID: ") + str(self.Professorennummer)
        return ret
    #als Alternative mit den F-Strings
    #f'{self.Professorennummer} ({self.Name})'



class Projekt(models.Model):
    ProjektID = models.AutoField(primary_key=True, null=False, unique=True)
    Name = models.CharField(max_length=128, null=True)

    Professorennummer_FK = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name


class Element(models.Model):
    ElementID = models.AutoField(primary_key=True, null=False, unique=True)

    Name = models.CharField(max_length=128, null=True)
    Kommentar = models.CharField(max_length=128, null=True)
    Datum_Erstellung = models.DateTimeField(auto_now_add=True)
    Datum_Aenderung = models.DateTimeField(auto_now=True)

    ProjektID_FK = models.ForeignKey('Projekt', on_delete=models.SET_NULL, null=True, blank=True)
    Matrikelnummer_FK = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name

class Requirement(models.Model):
    RequirementID = models.AutoField(primary_key=True, null=False, unique=True)

    Kategorie = models.CharField(
        max_length=1,
        choices=KATEGORIEN,
        blank=True,
        help_text='Kategorie des Requirements',
    )
    #um mit dem Nutzer zu verbinden
    ersteller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    ElementID_FK = models.ForeignKey('Element', on_delete=models.SET_NULL, null=True, blank=True)

#    class Meta:
#        permissions = (("can_mark_category", "Set a Category"), )



    #Man darf keine Schlüssel hier angeben
    def __str__(self):
        e = Element.objects.get(requirement__ElementID_FK=self.ElementID_FK)
        return "ID: " + str(self.RequirementID) + " Element-Name: " + str(e.Name)

    def get_absolute_url(self):
        return reverse('aut:requ_detail', args=[str(self.RequirementID)])




class TestCase(models.Model):
    TestCaseID = models.AutoField(primary_key=True, null=False, unique=True)

    Vorbedingung = models.CharField(max_length=128, null=True)
    Schritte = models.CharField(max_length=128, null=True)
    erwartetesErgebnis = models.CharField(max_length=128, null=True)
    tatsaechlichesErgebnis = models.CharField(max_length=128, null=True)

    ElementID_FK = models.ForeignKey('Element', on_delete=models.SET_NULL, null=True, blank=True)

    #def __str__(self):
    #    return self.TestCaseID

class TestRun(models.Model):
    TestRunID = models.AutoField(primary_key=True, null=False, unique=True)

    LOAN_STATUS = (
        ('p', 'pass'),
        ('f', 'fail'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        help_text='TestRun Ergebnis',
    )
    Dauer = models.FloatField(null=True)
    Datum_Durchführung = models.DateTimeField(auto_now_add=True) #Wird beim Erstellen geschrieben, macht Sinn da man danach nicht mehr verändert

    ElementID_FK = models.ForeignKey('Element', on_delete=models.SET_NULL, null=True, blank=True)
    TestCaseID_FK = models.ForeignKey('TestCase', on_delete=models.SET_NULL, null=True, blank=True)

    #def __str__(self):
    #    return self.TestRunID


class Student(models.Model):
    Matrikelnummer = models.AutoField(primary_key=True, null=False, unique=True)
    Name = models.CharField(max_length=128, null=True)
    Passwort = models.CharField(max_length=128, null=True)

    Gruppennummer_FK = models.ForeignKey('Projekt', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name

    def display_project(self):
        return (Projekt.objects.get(student__Gruppennummer_FK=self.Gruppennummer_FK)) #'9782a5ca-f7b6-4d52-9797-75790dd90c1e'
    display_project.short_description = 'ProjektName'

class Requirement_TestCase(models.Model):

    RequirementID_FK = models.ForeignKey('Requirement', on_delete=models.SET_NULL, null=True, blank=True)
    TestCaseID_FK = models.ForeignKey('TestCase', on_delete=models.SET_NULL, null=True, blank=True)

    #def __str__(self):
    #    return self.RequirementID_FK