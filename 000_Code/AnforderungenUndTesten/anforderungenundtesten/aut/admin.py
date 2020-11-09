from django.contrib import admin

# Register your models here.
from .models import Projekt, Requirement, TestRun, TestCase, Student, Professor, Requirement_TestCase, Element

#admin.site.register(Projekt)
admin.site.register(Requirement)
#admin.site.register(TestRun)
admin.site.register(TestCase)
#admin.site.register(Student)
admin.site.register(Requirement_TestCase)
admin.site.register(Element)
#admin.site.register(Professor)
#Die beiden Arten sind gleich in ihrer Funktion
#define the admin class
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('Professorennummer', 'Name', 'Passwort')

admin.site.register(Professor, ProfessorAdmin)

class StudentInline(admin.TabularInline):
    model = Student

@admin.register(Projekt)
class ProjektAdmin(admin.ModelAdmin):
    list_filter = ('ProjektID', 'Professorennummer_FK')
    inlines = [StudentInline]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Matrikelnummer', 'Name', 'Passwort', 'Gruppennummer_FK', 'display_project')


@admin.register(TestRun)
class TestRunAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info', {
            'fields': ('TestRunID', 'status', 'Dauer')
        }),
        ('Verbindungen', {
            'fields': ('ElementID_FK', 'TestCaseID_FK')
        }),
    )




