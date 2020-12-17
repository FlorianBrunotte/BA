from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# restrict access to logged in users with an check if he is authenticated
# see django docs
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import professor, projekt, student, requirement, testcase, testrun, testcase_schritt

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Wenn das alles geht fress ich einen Besen
from .forms import RequirementForm, TestCaseForm, TestRunForm, TestCase_Schritt_Form, TestCase_Schritt_Form2, GroupForm
from .choices import *
#Ende der Imports
########################################################################################################################

@login_required()
def view_dashboard(request):
    #User erhalten und allgemeine Informationen
    user = User.objects.get(username=request.user.username)
    user_gruppennummer = user.user_erweitern.gruppennummer
    all_users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)

#Requirements
########################################################################################################################
    #Code um die Elemente der eigenen Gruppe zu bekommen
    #Nur mit dem req_for_usergroup arbeiten
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    req_for_usergroup = requirement.objects.filter(req_fk_ersteller__in=users)
    num_req = req_for_usergroup.count()

    #eigene Requirements
    num_req_eigene = req_for_usergroup.filter(req_fk_ersteller=request.user)
    num_req_eigene = num_req_eigene.count()

    #abgedeckte Requirements = Requiremtens mit TestCase
    lis_no_testcase = []
    lis_yes_testcase = []
    for req in req_for_usergroup:
        if req.testcase_set.all().exists():
            lis_yes_testcase.append(req)
        else: #wenn es kein TestCase gibt
            lis_no_testcase.append(req)
    num_yes_testcase = len(lis_yes_testcase)
    num_no_testcase = len(lis_no_testcase)

#TestCases
########################################################################################################################
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    testc_for_usergroup = testcase.objects.filter(testc_fk_ersteller__in=users)
    num_testc = testc_for_usergroup.count()

    #eigene TestCases
    num_testc_eigene = testc_for_usergroup.filter(testc_fk_ersteller=request.user)
    num_testc_eigene = num_testc_eigene.count()

    #abgedeckte Requirements = Requiremtens mit TestCase
    lis_no_testrun_or_no_run = [] #enthält testcase ohne TestRun und mit TestRun der noch nicht lief
    lis_yes_testrun_run_failed = []
    lis_yes_testrun_run_passed = []

    for testc in testc_for_usergroup:
        if testc.testrun_set.all().exists():
            if testc.testrun_set.all().latest('testr_datum_aenderung').testr_status == 'f': #failed
                lis_yes_testrun_run_failed.append(testc)

            elif testc.testrun_set.all().latest('testr_datum_aenderung').testr_status == 'p':
                lis_yes_testrun_run_passed.append(testc)

            elif testc.testrun_set.all().latest('testr_datum_aenderung').testr_status == 'n': #no run yet
                lis_no_testrun_or_no_run.append(testc)

        else: #wenn es kein TestRun gibt
            lis_no_testrun_or_no_run.append(testc)

    num_lis_no_testrun_or_no_run = len(lis_no_testrun_or_no_run)
    num_lis_yes_testrun_run_failed = len(lis_yes_testrun_run_failed)
    num_lis_yes_testrun_run_passed = len(lis_yes_testrun_run_passed)

#TestRuns
########################################################################################################################
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    testr_for_usergroup = testrun.objects.filter(testr_fk_ersteller__in=users)
    num_testr = testr_for_usergroup.count()
    num_lis_no_testrun = testr_for_usergroup.filter(testr_status='n')
    num_lis_failed_testrun = testr_for_usergroup.filter(testr_status='f')
    num_lis_passed_testrun = testr_for_usergroup.filter(testr_status='p')

    num_lis_no_testrun = len(num_lis_no_testrun)
    num_lis_failed_testrun = len(num_lis_failed_testrun)
    num_lis_passed_testrun = len(num_lis_passed_testrun)


    if request.user.user_erweitern.rolle == 's':
        #Student Seite
        pass


    if request.user.user_erweitern.rolle == 'p':
        #Professor Seite
        if request.method == 'POST':
            form = GroupForm(request.POST)
            if form.is_valid():
                user.user_erweitern.gruppennummer = form.cleaned_data['group_form_group']
                user.user_erweitern.save()

                # request.user.save()
                return HttpResponseRedirect(reverse('aut:view_dashboard'))
        else:
            form = GroupForm(initial={'group_form_group': user.user_erweitern.gruppennummer,
                                      })
        #Context übergeben mit der Form
        context = {
            'user_gruppennummer': user_gruppennummer,
            'all_users': all_users,

            'num_req': num_req,
            'num_req_eigene': num_req_eigene,
            'num_yes_testcase': num_yes_testcase,
            'num_no_testcase': num_no_testcase,

            'num_testc': num_testc,
            'num_testc_eigene': num_testc_eigene,
            'num_lis_no_testrun_or_no_run': num_lis_no_testrun_or_no_run,
            'num_lis_yes_testrun_run_failed': num_lis_yes_testrun_run_failed,
            'num_lis_yes_testrun_run_passed': num_lis_yes_testrun_run_passed,

            'num_testr': num_testr,
            'num_lis_no_testrun': num_lis_no_testrun,
            'num_lis_failed_testrun': num_lis_failed_testrun,
            'num_lis_passed_testrun': num_lis_passed_testrun,

            'form': form,
        }
        return render(request, 'aut/010_dashboard.html', context=context)

    context = {
        'user_gruppennummer': user_gruppennummer,
        'all_users': all_users,

        'num_req': num_req,
        'num_req_eigene': num_req_eigene,
        'num_yes_testcase': num_yes_testcase,
        'num_no_testcase': num_no_testcase,

        'num_testc': num_testc,
        'num_testc_eigene': num_testc_eigene,
        'num_lis_no_testrun_or_no_run': num_lis_no_testrun_or_no_run,
        'num_lis_yes_testrun_run_failed': num_lis_yes_testrun_run_failed,
        'num_lis_yes_testrun_run_passed': num_lis_yes_testrun_run_passed,

        'num_testr': num_testr,
        'num_lis_no_testrun': num_lis_no_testrun,
        'num_lis_failed_testrun': num_lis_failed_testrun,
        'num_lis_passed_testrun': num_lis_passed_testrun,
    }
    return render(request, 'aut/010_dashboard.html', context=context)


def view_dashboard_prof(request):
    user = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            user.user_erweitern.gruppennummer = form.cleaned_data['group_form_group']
            user.user_erweitern.save()

            #request.user.save()
            return HttpResponseRedirect(reverse('aut:view_dashboard_prof'))
    else:
        form = GroupForm(initial={'group_form_group': user.user_erweitern.gruppennummer,
                                   })




    num_req = requirement.objects.all().count()
   # num_visits = request.session.get('num_visits', 0)
    #request.session['num_visits'] = num_visits + 1
    num_visits = 999
    context = {
        'num_req': num_req,
        'num_visits': num_visits,
        'form': form,
    }
    return render(request, 'aut/010_dashboard_prof.html', context=context)

#Ende der Dashboards
########################################################################################################################

def view_requirement(request):
    users = User.objects.filter(user_erweitern__gruppennummer=request.user.user_erweitern.gruppennummer)
    req_for_usergroup = requirement.objects.filter(req_fk_ersteller__in=users)

    context = {
        'requirements': req_for_usergroup,
    }
    return render(request, 'aut/010_requirement.html', context=context)

#add save mit dem user
def requirement_change(request, pk):
    requ_instance = get_object_or_404(requirement, req_pk_requirementid=pk)

    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            requ_instance.req_kategorie = form.cleaned_data['form_category']
            requ_instance.req_kommentar = form.cleaned_data['req_form_kommentar']
            requ_instance.req_name = form.cleaned_data['req_form_name']
            requ_instance.req_beschreibung = form.cleaned_data['req_form_beschreibung']

            requ_instance.save()
            return HttpResponseRedirect(reverse('aut:requirement_change', kwargs={'pk': pk}))
    else:
      form = RequirementForm(initial={'form_category': KATEGORIEN,
                                      'req_form_kommentar': requ_instance.req_kommentar,
                                      'req_form_name': requ_instance.req_name,
                                      'req_form_beschreibung': requ_instance.req_beschreibung,})

    # else wird erstmal nicht gemacht

    context = {
        'form': form,
        'requ_instance': requ_instance,
    }

    return render(request, 'aut/020_requirement_anpassen.html', context)



class requirementCreate(CreateView):
    model = requirement
    fields = '__all__'
    template_name = 'aut/020_requirement_form.html'

class requirementCreateAndTestCase(CreateView):
    model = requirement
    fields = '__all__'
    template_name = 'aut/020_requirement_form_and_testcase.html'

#Ende der Requirements
########################################################################################################################

def view_testcase(request):
    testcases = testcase.objects.all()
    context = {
        'testcases': testcases,
    }
    return render(request, 'aut/010_testcase.html', context=context)


########################################################################################################################
def testcase_create(request, pk=None):
    testc_instance, created = testcase.objects.get_or_create(
        testc_pk_testcaseid=pk,
    )

    # RequirementID anstatt pkk = pK vieleicht
    if request.method == 'POST':
        print(request.POST)
        form = TestCaseForm(request.POST)
        schritt_form = TestCase_Schritt_Form(request.POST)

        if request.POST.get("delete_testcase"):
            name = "ID:" + str(testc_instance.testc_pk_testcaseid) + " Name: " + str(testc_instance.testc_name)
            testc_instance.delete()
            return HttpResponse(name + " wurde gelöscht")
            #return HttpResponse("<script>parent.location.reload();</script>")
            #return HttpResponseRedirect(reverse('aut:view_testcase'))

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

                                     })

    # else wird erstmal nicht gemacht
    schritte_instance = testcase_schritt.objects.filter(schritt_fk_testcase=testc_instance)
    context = {
        'form': form,
        'schritt_form': schritt_form,
        'testc_instance': testc_instance,
        'schritte_instance': schritte_instance,
    }
    print("Render")
    return render(request, 'aut/020_testcase_anpassen.html', context)

#Ende der TestCases
########################################################################################################################

def view_testrun(request):
    testruns = testrun.objects.all()
    context = {
        'testruns': testruns,
    }
    return render(request, 'aut/010_testrun.html', context=context)

#Hier wird getestet
def testrun_change(request, pk=None, fk=None):
    testr_instance, created = testrun.objects.get_or_create(
        testr_pk_testrunid=pk,
    )
    #testr_instance = get_object_or_404(testrun, testr_pk_testrunid=pk)

    # RequirementID anstatt pkk = pK vieleicht
    if request.method == 'POST':
        form = TestRunForm(request.POST)
        if form.is_valid():
            testr_instance.testr_name = form.cleaned_data['testr_form_name']
            testr_instance.testr_kommentar = form.cleaned_data['testr_form_kommentar']
            testr_instance.testr_beschreibung = form.cleaned_data['testr_form_beschreibung']
            testr_instance.testr_status = form.cleaned_data['testr_form_status']
            testr_instance.testr_fk_testcaseid = form.cleaned_data['testr_form_fk_testcase']

            testr_instance.save()
            return HttpResponseRedirect(reverse('aut:testrun_change', kwargs={'pk': pk}))
    else:
      form = TestRunForm(initial={'testr_form_name': testr_instance.testr_name,
                                      'testr_form_kommentar': testr_instance.testr_kommentar,
                                      'testr_form_beschreibung': testr_instance.testr_beschreibung,
                                      'testr_form_status': testr_instance.testr_status,
                                         'testr_form_fk_testcase':fk,
                                 #'testr_form_fk_testcase':testr_instance.testr_fk_testcaseid

                                      })

    # else wird erstmal nicht gemacht

    context = {
        'form': form,
        'testr_instance': testr_instance,
    }

    return render(request, 'aut/020_testrun_anpassen.html', context)

class testrunCreate(CreateView):
    model = testrun
    fields = '__all__'
    template_name = 'aut/020_testrun_form.html'

class testrunCreateAndRun(CreateView):
    model = testrun
    fields = '__all__'
    template_name = 'aut/020_testrun_form_and_run.html'

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







def view_projekt(request):
    return render(request, 'aut/010_projekt.html')




class RequirementByUser(LoginRequiredMixin, generic.ListView):
    model = requirement
    template_name = 'aut/requirement_by_user.html'

    def get_queryset(self):
        return view_requirement.objects.filter(ersteller=self.request.user)


# Variablen können auch übergeben werden, hiermit wird die aktuelle Zeit übergeben bei der Erstellung von runserver nicht wenn die Webseite aufgerufen wird
import datetime

now = datetime.datetime.now()


def firstview(request):
    return HttpResponse("Hallo das hier ist meine erste View, Seite wurde erstellt am: " + str(now))


def index2(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/010_testrun.html')




# View die nur ein Requirement anzeigt
def detail_requirement(request, req_id):
    return HttpResponse("You are looking at requirement %s" % req_id)


# Idee für eine Liste mit den Werten für einen Key
def projektbyprof(request, profid):
    ret = []
    for value in projekt.objects.filter(Professorennummer_FK=profid):  # '9782a5ca-f7b6-4d52-9797-75790dd90c1e'
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
    num_req = requirement.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_req': num_req,
        'num_visits': num_visits,
    }
    return render(request, 'aut/010_dashboard.html', context=context)


# Die Projekt ID sollte irgendwie von außen kommen, vielleicht mit Forms
def req_list_view(request):
    re = []
    truere = []
    dic = {}
    i = 0
    for value in view_requirement.objects.filter(
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

    # template = loader.get_template('aut/010_requirement.html')
    context = {  # vorher re
        're': truere,  # von dem Template links zu Python rechts oder einfach immer gleicher Name
    }

    # return HttpResponse(template.render(context, request))
    # mit der render FUnktion kann man ein eAbkürzung machen
    return render(request, 'aut/010_requirement.html', context)


class RequListView(generic.ListView):
    model = view_requirement
    # Filter für zum Beispiel die Projekte die zu dem eingeloggten Studenten gehören


# View die nur ein Requirement anzeigt
class RequirementListViewDetail(generic.DetailView):
    model = requirement



def testrun_machen(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/testrun_durchf_hren.html')


def statistik(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/010_statistik.html')



def abmelden(request):
    #  return HttpResponse(now) #"Moin Leute. Hier ist der Index der App"
    return render(request, 'aut/abmelden.html')


