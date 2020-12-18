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


<<<<<<< Updated upstream
def anpassen_requirement(request, pk):
    requ_instance = get_object_or_404(Requirement, pk=pk)

    # RequirementID anstatt pkk = pK vieleicht
=======
#Ende des Dashboards
########################################################################################################################
def view_requirement(request):
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    req_for_usergroup = requirement.objects.filter(req_fk_ersteller__in=users)

    context = {
        'requirements': req_for_usergroup,
    }
    return render(request, 'aut/010_requirement.html', context=context)

########################################################################################################################
def edit_requirement(request, pk=None):
    requ_instance, created = requirement.objects.get_or_create(req_pk_requirementid=pk, )

>>>>>>> Stashed changes
    if request.method == 'POST':
        form = RequirementForm(request.POST)

        if request.POST.get("delete_requirement"):
            name = "ID:" + str(requ_instance.req_pk_requirementid) + " Name: " + str(requ_instance.req_name)
            requ_instance.delete()
            return HttpResponse(name + " wurde gelöscht")

        if form.is_valid():
<<<<<<< Updated upstream
            requ_instance.Kategorie = form.cleaned_data['form_category']
=======
            requ_instance.req_kategorie = form.cleaned_data['form_category']
            requ_instance.req_kommentar = form.cleaned_data['req_form_kommentar']
            requ_instance.req_name = form.cleaned_data['req_form_name']
            requ_instance.req_beschreibung = form.cleaned_data['req_form_beschreibung']
            requ_instance.req_fk_ersteller = request.user

>>>>>>> Stashed changes
            requ_instance.save()
            return HttpResponseRedirect(reverse('aut:anpassen_requ', kwargs={'pk': pk}))
    else:
<<<<<<< Updated upstream
      form = RequirementForm(initial={'form_category': KATEGORIEN })
=======
      form = RequirementForm(initial={'form_category': requ_instance.req_kategorie,
                                      'req_form_kommentar': requ_instance.req_kommentar,
                                      'req_form_name': requ_instance.req_name,
                                      'req_form_beschreibung': requ_instance.req_beschreibung,})
>>>>>>> Stashed changes

    # else wird erstmal nicht gemacht

    context = {
        'form': form,
        'requ_instance': requ_instance,
    }

<<<<<<< Updated upstream
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
=======
    return render(request, 'aut/020_requirement_anpassen.html', context)

#Ende der Requirements
########################################################################################################################

def view_testcase(request):
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    testc_for_usergroup = testcase.objects.filter(testc_fk_ersteller__in=users)

    context = {
        'testcases': testc_for_usergroup,
    }
    return render(request, 'aut/010_testcase.html', context=context)

########################################################################################################################
def edit_testcase(request, pk=None):
    testc_instance, created = testcase.objects.get_or_create(testc_pk_testcaseid=pk,)
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    req_for_usergroup = requirement.objects.filter(req_fk_ersteller__in=users)

    # RequirementID anstatt pkk = pK vieleicht
    if request.method == 'POST':
        form = TestCaseForm(request.POST, reqs=req_for_usergroup)
        schritt_form = TestCase_Schritt_Form(request.POST)

        if request.POST.get("delete_testcase"):
            name = "ID:" + str(testc_instance.testc_pk_testcaseid) + " Name: " + str(testc_instance.testc_name)
            testc_instance.delete()
            return HttpResponse(name + " wurde gelöscht")

        if request.POST.get("delete_schritt"):
            delete_schritt = int(request.POST.get("delete_schritt"))
            delete = testcase_schritt.objects.get(schritt_pk_id=delete_schritt)
            # This will delete the Blog and all of its Entry objects.
            delete.delete()
            return HttpResponseRedirect(reverse('aut:testcase_change', kwargs={'pk': testc_instance.testc_pk_testcaseid}))

        if schritt_form.is_valid():
            test_schritt = testcase_schritt(schritt_pk_id=None, schritt_fk_testcase=testc_instance)
            test_schritt.schritt_schritte = schritt_form.cleaned_data['schritt_form_schritt']
            test_schritt.schritt_erwartetesergebnis = schritt_form.cleaned_data['schritt_form_erwartetesergebnis']
            test_schritt.save()
            return HttpResponseRedirect(reverse('aut:testcase_change', kwargs={'pk': testc_instance.testc_pk_testcaseid}))

        if form.is_valid():
            testc_instance.testc_vorbedingung = form.cleaned_data['testc_form_vorbedingung']
            testc_instance.testc_kommentar = form.cleaned_data['testc_form_kommentar']
            testc_instance.testc_name = form.cleaned_data['testc_form_name']
            testc_instance.testc_beschreibung = form.cleaned_data['testc_form_beschreibung']
            testc_instance.testc_fk_requirement.set(form.cleaned_data['testc_form_fk_requirement'])
            testc_instance.testc_fk_ersteller = request.user

            testc_instance.save()

            return HttpResponseRedirect(reverse('aut:testcase_change', kwargs={'pk': testc_instance.testc_pk_testcaseid}))
    else:

        schritt_form = TestCase_Schritt_Form()
        form = TestCaseForm(initial={'testc_form_name': testc_instance.testc_name,
                                      'testc_form_beschreibung': testc_instance.testc_beschreibung,
                                      'testc_form_kommentar': testc_instance.testc_kommentar,
                                      'testc_form_vorbedingung': testc_instance.testc_vorbedingung,
                                      'testc_form_fk_requirement': requirement.objects.filter(testcase=testc_instance),

                                     }, reqs=req_for_usergroup)

    # else wird erstmal nicht gemacht
    schritte_instance = testcase_schritt.objects.filter(schritt_fk_testcase=testc_instance)
    context = {
        'form': form,
        'schritt_form': schritt_form,
        'testc_instance': testc_instance,
        'schritte_instance': schritte_instance,
    }

    return render(request, 'aut/020_testcase_anpassen.html', context)

#Ende der TestCases
########################################################################################################################

def view_testrun(request):
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    testr_for_usergroup = testrun.objects.filter(testr_fk_ersteller__in=users)

    context = {
        'testruns': testr_for_usergroup,
    }
    return render(request, 'aut/010_testrun.html', context=context)

#Hier wird getestet
def edit_testrun(request, pk=None):
    testr_instance, created = testrun.objects.get_or_create(testr_pk_testrunid=pk,)
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    testc_for_usergroup = testcase.objects.filter(testc_fk_ersteller__in=users)

    if request.method == 'POST':
        form = TestRunForm(request.POST,tecs=testc_for_usergroup)

        if request.POST.get("delete_testrun"):
            name = "ID:" + str(testr_instance.testr_pk_testrunid) + " Name: " + str(testr_instance.testr_name)
            testr_instance.delete()
            return HttpResponse(name + " wurde gelöscht")

        if form.is_valid():
            testr_instance.testr_name = form.cleaned_data['testr_form_name']
            testr_instance.testr_kommentar = form.cleaned_data['testr_form_kommentar']
            testr_instance.testr_beschreibung = form.cleaned_data['testr_form_beschreibung']
            testr_instance.testr_status = form.cleaned_data['testr_form_status']
            testr_instance.testr_fk_testcaseid = form.cleaned_data['testr_form_fk_testcase']
            testr_instance.testr_fk_ersteller = request.user
            testr_instance.save()
            return HttpResponseRedirect(reverse('aut:testrun_change', kwargs={'pk': pk}))
    else:
      form = TestRunForm(initial={'testr_form_name': testr_instance.testr_name,
                                      'testr_form_kommentar': testr_instance.testr_kommentar,
                                      'testr_form_beschreibung': testr_instance.testr_beschreibung,
                                      'testr_form_status': testr_instance.testr_status,
                                    'testr_form_fk_testcase':testr_instance.testr_fk_testcaseid

                                      },tecs=testc_for_usergroup)

    # else wird erstmal nicht gemacht

    context = {
        'form': form,
        'testr_instance': testr_instance,
    }

    return render(request, 'aut/020_testrun_anpassen.html', context)

def testrun_run(request, pk):
    testr_instance = get_object_or_404(testrun, testr_pk_testrunid=pk)
    testr_schritte = testcase_schritt.objects.filter(schritt_fk_testcase=testr_instance.testr_fk_testcaseid)
#hier die Form mit den 2 Feldern die man braucht
    if request.method == 'POST':
        print(request.POST)
        schritt_form = TestCase_Schritt_Form2(request.POST)

        update_schritt = int(request.POST.get("update_schritt"))
        which_update_schritt = testcase_schritt.objects.get(schritt_pk_id=update_schritt)

        if schritt_form.is_valid():
            which_update_schritt.schritt_tatsaechlichesergebnis = schritt_form.cleaned_data['schritt_form_tatsaechlichesergebnis']
            which_update_schritt.schritt_ergebnis = schritt_form.cleaned_data['schritt_ergebnis']
            which_update_schritt.save()
            return HttpResponseRedirect(reverse('aut:testrun_run', kwargs={'pk': testr_instance.testr_pk_testrunid}))

    else:
        schritt_form = TestCase_Schritt_Form2()

    context = {
        'testr_instance': testr_instance,
        'testr_schritte': testr_schritte,
        'schritt_form': schritt_form,
    }

    return render(request, 'aut/020_testrun_run.html', context)

#Ende der TestRuns
########################################################################################################################

def view_statistik(request):

    #TestCase Coverage: Requriements mit TestCase / alle Requirements
    #Für die Gruppe die Requirements
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    req_for_usergroup = requirement.objects.filter(req_fk_ersteller__in=users)

    int_req_with_testcase = 0
    for req in req_for_usergroup:
        if req.testcase_set.all().exists():
            int_req_with_testcase += 1
    num_req = req_for_usergroup.count()
    TestCase_Coverage = int_req_with_testcase/num_req * 100 #Für Prozent

    #TestRun Coverage: Requirement mit erfolgreichem TestRun / alle Requirements
    #Für die Gruppe die Requirements
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    req_for_usergroup = requirement.objects.filter(req_fk_ersteller__in=users)

    int_req_with_testrun = 0
    for req in req_for_usergroup:
        if req.testcase_set.all().exists():
            for testc in req.testcase_set.all():
                if testc.testrun_set.all().exists():
                    if testc.testrun_set.all().latest('testr_datum_aenderung').testr_status == 'p':
                        int_req_with_testrun += 1

    num_req = req_for_usergroup.count()
    TestRun_Coverage = int_req_with_testrun/num_req * 100 #Für Prozent

    #Alle ELemente für eine Gruppe
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    req_for_usergroup = requirement.objects.filter(req_fk_ersteller__in=users)
    testc_for_usergroup = testcase.objects.filter(testc_fk_ersteller__in=users)
    testr_for_usergroup = testrun.objects.filter(testr_fk_ersteller__in=users)



    context = {
        'all_requirements': req_for_usergroup,
        'all_testcases': testc_for_usergroup,
        'all_testruns': testr_for_usergroup,
        'TestCase_Coverage': TestCase_Coverage,
        'TestRun_Coverage': TestRun_Coverage,
    }


    return render(request, 'aut/010_statistik.html', context)






>>>>>>> Stashed changes


def anmelden(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/anmelden.html')


<<<<<<< Updated upstream
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

=======
>>>>>>> Stashed changes

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
