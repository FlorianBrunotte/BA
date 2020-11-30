from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# restrict access to logged in users with an check if he is authenticated
# see django docs
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Professor, Element, Projekt, Student, Requirement, Requirement_TestCase, TestCase, TestRun

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Wenn das alles geht fress ich einen Besen
from .forms import RequirementForm
from .choices import *


def anpassen_requirement(request, pk):
    requ_instance = get_object_or_404(Requirement, pk=pk)

    # RequirementID anstatt pkk = pK vieleicht
    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            requ_instance.Kategorie = form.cleaned_data['form_category']
            requ_instance.save()
            return HttpResponseRedirect(reverse('aut:anpassen_requ', kwargs={'pk': pk}))
    else:
      form = RequirementForm(initial={'form_category': KATEGORIEN })

    # else wird erstmal nicht gemacht

    context = {
        'form': form,
        'requ_instance': requ_instance,
    }

    return render(request, 'aut/requirement_detail.html', context)


class RequirementByUser(LoginRequiredMixin, generic.ListView):
    model = Requirement
    template_name = 'aut/requirement_by_user.html'

    def get_queryset(self):
        return Requirement.objects.filter(ersteller=self.request.user)


# Variablen können auch übergeben werden, hiermit wird die aktuelle Zeit übergeben bei der Erstellung von runserver nicht wenn die Webseite aufgerufen wird
import datetime

now = datetime.datetime.now()


def firstview(request):
    return HttpResponse("Hallo das hier ist meine erste View, Seite wurde erstellt am: " + str(now))


def index2(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/testrun.html')


def requirement(request):
    return render(request, 'aut/requirement.html')


# View die nur ein Requirement anzeigt
def detail_requirement(request, req_id):
    return HttpResponse("You are looking at requirement %s" % req_id)


# Idee für eine Liste mit den Werten für einen Key
def projektbyprof(request, profid):
    ret = []
    for value in Projekt.objects.filter(Professorennummer_FK=profid):  # '9782a5ca-f7b6-4d52-9797-75790dd90c1e'
        ret.append(value)

    return HttpResponse(ret)


from django.template import loader


# Problem kann nicht an ein Projekt gebunden werden mit dem jetztigen ER Modell
# Vielleicht IS A Beziehung rausmachen


def anmelden(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/anmelden.html')


# use a decorater to restrict access
@login_required
def dash(request):
    num_req = Requirement.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_req': num_req,
        'num_visits': num_visits,
    }
    return render(request, 'aut/dashboard.html', context=context)


# Die Projekt ID sollte irgendwie von außen kommen, vielleicht mit Forms
def req_list_view(request):
    re = []
    truere = []
    dic = {}
    i = 0
    for value in Requirement.objects.filter(
            ElementID_FK__ProjektID_FK=3).values():  # returns Queryset Filtern nach Projekt, was woanders herommen muss
        re.append(value)
        for e in Element.objects.filter(ElementID=value[
            'ElementID_FK_id']).values():  # returns Queryset, gibt alle entsprechenden Elemente wieder und man kann auf die Sachen zugreifen
            re[i].update(e)  # liste von Dictionarys

        dic['ID'] = re[i]['RequirementID']
        dic['Name'] = re[i]['Name']
        dic['Kommentar'] = re[i]['Kommentar']

        truere.append(dic.copy())  # wenn man das nicht macht klappt das nicht, dann hat man nur eine Referenz
        # auf das Dictionary. Mit Copy hat man dann eine Kopie
        i = i + 1

    # template = loader.get_template('aut/requirement.html')
    context = {  # vorher re
        're': truere,  # von dem Template links zu Python rechts oder einfach immer gleicher Name
    }

    # return HttpResponse(template.render(context, request))
    # mit der render FUnktion kann man ein eAbkürzung machen
    return render(request, 'aut/requirement.html', context)


class RequListView(generic.ListView):
    model = Requirement
    # Filter für zum Beispiel die Projekte die zu dem eingeloggten Studenten gehören


# View die nur ein Requirement anzeigt
class RequListViewDetail(generic.DetailView):
    model = Requirement


def testcase(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/testcase.html')


def testrun(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/testrun.html')


def testrun_machen(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/testrun_durchf_hren.html')


def statistik(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/statistik.html')


def projekt(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/projekt.html')


def abmelden(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/abmelden.html')
# anmelden
# dash
# requirement
# testcase
# testrun
# testrun machen
# statistik
# projekt
# abmelden
