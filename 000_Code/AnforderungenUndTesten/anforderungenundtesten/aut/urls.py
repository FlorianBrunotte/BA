from django.urls import path, include, re_path
from django.views.generic import RedirectView

from . import views

#Name der App
app_name = 'aut'
urlpatterns = [
    # Für dieses Requirement die Form
    #   path('requ/<int:pk>/anpassen', views.anpassen_requirement, name='anpassen_requ'),

    #Basis Views
    path('', views.view_dashboard, name='view_dashboard'), #vielleicht noch verschönern
    path('dashboard_prof', views.view_dashboard_prof, name='view_dashboard_prof'), #vielleicht noch verschönern
    path('requirement', views.view_requirement, name='view_requirement'),
    path('testcase', views.view_testcase, name='view_testcase'),
    path('testrun', views.view_testrun, name='view_testrun'),
    path('statistik', views.view_statistik, name='view_statistik'),

    #Requirement Views für die Forms
    path('requirement/<int:pk>/', views.requirement_change, name='requirement_change'),
    path('requirement/create/', views.requirementCreate.as_view(), name='requirement_create'),
    path('requirement/create_and_testcase', views.requirementCreateAndTestCase.as_view(), name='requirement_create_and_testcase'),

    #TestCase Views für die Forms
    #path('testcase/<int:pk>/', views.testcase_change, name='testcase_change'),
#    path('testcase/create', views.testcaseCreate.as_view(), name='testcase_create'),

    path('testcase/<int:pk>/', views.testcase_create, name='testcase_change'),
    path('testcase/create/', views.testcase_create, name='testcase_create'),
    path('testcase/create/<int:pk>/', views.testcase_create, name='testcase_create'),

    #TestRun Views für die Forms
    path('testrun/<int:pk>/', views.testrun_change, name='testrun_change'),
    path('testrun/create', views.testrun_change, name='testrun_create'),
    path('testrun/create/<int:pk>/', views.testrun_change, name='testrun_create'),
    path('testrun/create_2/<int:fk>/', views.testrun_change, name='testrun_create_2'),

    path('testrun/create_and_run', views.testrunCreateAndRun.as_view(), name='testrun_create_and_run'),
    path('testrun/run/<int:pk>/', views.testrun_run, name='testrun_run'),

   # path('testrun/<int:pk>/', views.testrun_change, name='testrun_change'),
   # path('testrun/create', views.testrunCreate.as_view(), name='testrun_create'),

    #alte Sachen


#    path('', views.anmelden, name='anmelden'),
 #   path('dashboard', views.dash, name='dash'), #hier steht nix ist aber unter /polls/ weil das in dem Haupt url File steht
    path('b', views.index2, name='index2'),
    path('firstview', views.firstview, name='firstview'),

    path('requs/', views.RequListView.as_view(), name='requ'),
 #   path('requ/<int:req_id>/', views.detail_requirement, name='detail_req'),
    #Detail eines Requirement




    path('prof/<int:profid>/', views.projektbyprof, name='detail_projekt'),


 #   path('requirements', views.req_list_view, name='req'),
   # path('testcases', views.testcase, name='testc'),
  #  path('testruns', views.testrun, name='testr'),
    path('testruns_durchführen', views.testrun_machen, name='testrd'),
    path('statistiken', views.statistik, name='stat'),
    path('projekt', views.projekt, name='pro'),
    path('abmelden', views.abmelden, name='abmelden'),
    path('requuser', views.RequirementByUser.as_view(), name='requbyuser')



    #anmelden
    #dash
    #requirement
    #testcase
    #testrun
    #testrun machen
    #statistik
    #projekt
    #abmelden

]

