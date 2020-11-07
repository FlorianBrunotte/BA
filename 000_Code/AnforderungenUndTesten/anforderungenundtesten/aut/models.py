from django.db import models
import datetime
# Create your models here.
import uuid  # Für den Primary Key


class Professor(models.Model):
    Professorennummer = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Zum Anmelden')
    Name = models.CharField(max_length=128, null=True)
    Passwort = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.Name


class Projekt(models.Model):
    ProjektID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identifikation der Projekte')
    Name = models.CharField(max_length=128, null=True)

    Professorennummer_FK = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name

class Element(models.Model):
    ElementID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identifikation der Elements')
    Name = models.CharField(max_length=128, null=True)
    Kommentar = models.CharField(max_length=128, null=True)
    Datum_Erstellung = models.DateTimeField(auto_now_add=True)
    Datum_Aenderung = models.DateTimeField(auto_now=True)

    ProjektID_FK = models.ForeignKey('Projekt', on_delete=models.SET_NULL, null=True)
    Matrikelnummer_FK = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name

class Requirement(models.Model):
    RequirementID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identifikation der Requirements')
    KATEGORIEN = (
        ('1', 'Kategorie 1'),
        ('2', 'Kategorie 2'),
    )
    Kategorie = models.CharField(
        max_length=1,
        choices=KATEGORIEN,
        blank=True,
        help_text='Kategorie des Requirements',
    )

    ElementID_FK = models.ForeignKey('Element', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.RequirementID

class TestCase(models.Model):
    TestCaseID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identifikation der TestCases')
    Vorbedingung = models.CharField(max_length=128, null=True)
    Schritte = models.CharField(max_length=128, null=True)
    erwartetesErgebnis = models.CharField(max_length=128, null=True)
    tatsaechlichesErgebnis = models.CharField(max_length=128, null=True)

    ElementID_FK = models.ForeignKey('Element', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.TestCaseID

class TestRun(models.Model):
    TestRunID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identifikation der TestRuns')
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

    ElementID_FK = models.ForeignKey('Element', on_delete=models.SET_NULL, null=True)
    TestCaseID_FK = models.ForeignKey('TestCase', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.TestRunID


class Student(models.Model):
    Matrikelnummer = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Zum Anmelden')
    Name = models.CharField(max_length=128, null=True)
    Passwort = models.CharField(max_length=128, null=True)

    Gruppennummer_FK = models.ForeignKey('Projekt', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name

class Requirement_TestCase(models.Model):

    RequirementID_FK = models.ForeignKey('Requirement', on_delete=models.SET_NULL, null=True)
    TestCaseID_FK = models.ForeignKey('TestCase', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.RequirementID_FK