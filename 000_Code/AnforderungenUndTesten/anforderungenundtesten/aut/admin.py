from django.contrib import admin

# Register your models here.
from .models import Projekt, Requirement, TestRun, TestCase

admin.site.register(Projekt)

admin.site.register(Requirement)

admin.site.register(TestRun)

admin.site.register(TestCase)