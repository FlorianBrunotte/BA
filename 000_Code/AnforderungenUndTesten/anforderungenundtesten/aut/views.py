from django.shortcuts import render
from .models import Student, Projekt, Professor, Element, TestCase, TestRun, Requirement, Requirement_TestCase


# Create your views here.

from django.http import HttpResponse


#Variablen können auch übergeben werden, hiermit wird die aktuelle Zeit übergeben bei der Erstellung von runserver nicht wenn die Webseite aufgerufen wird
import datetime
now = datetime.datetime.now()

def index(request):
    #return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    #generate Counts:
    num_student = Student.objects.all().count()
    num_req = Requirement.objects.all().count()
    context = {
        'num_student':num_student,
        'num_req':num_req,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class RequirementView(generic.ListView):
    model = Requirement
    context_object_name = 'req_list'
    template_name = 'aut/req_list.html'

    def get_context_data(self, **kwargs):
        context = super(RequirementView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class RequirementDetail(generic.DetailView):
    model = Requirement
    context_object_name = 'req_detail'
    template_name = 'aut/req_detail.html'