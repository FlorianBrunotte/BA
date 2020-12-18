from django.urls import path, include, re_path

from . import  views

#auf die Namen aufpassen ob die irgendwo bbenutzt werden
app_name = 'aut'
urlpatterns = [
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    path('', views.anmelden, name='anmelden'),
    path('dashboard', views.dash, name='dash'), #hier steht nix ist aber unter /polls/ weil das in dem Haupt url File steht
    path('b', views.index2, name='index2'),
    path('firstview', views.firstview, name='firstview'),

    path('requs/', views.RequListView.as_view(), name='requ'),
 #   path('requ/<int:req_id>/', views.detail_requirement, name='detail_req'),
    #Detail eines Requirement
    path('requ/<int:pk>/', views.RequListViewDetail.as_view(), name='requ_detail'),
    #Für dieses Requirement die Form
    path('requ/<int:pk>/anpassen', views.anpassen_requirement, name='anpassen_requ'),



    path('prof/<int:profid>/', views.projektbyprof, name='detail_projekt'),


    path('requirements', views.req_list_view, name='req'),
    path('testcases', views.testcase, name='testc'),
    path('testruns', views.testrun, name='testr'),
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

=======
=======
>>>>>>> Stashed changes
    #Basis Views
    path('', views.view_dashboard, name='view_dashboard'), #vielleicht noch verschönern
    path('requirement', views.view_requirement, name='view_requirement'),
    path('testcase', views.view_testcase, name='view_testcase'),
    path('testrun', views.view_testrun, name='view_testrun'),
    path('statistik', views.view_statistik, name='view_statistik'),

    #Requirement Views für die Forms
    path('requirement/<int:pk>/', views.edit_requirement, name='requirement_change'),
    path('requirement/create/', views.edit_requirement, name='requirement_create'),
    path('requirement/create/<int:pk>/', views.edit_requirement, name='requirement_create'),

    #TestCase Views für die Forms
    path('testcase/<int:pk>/', views.edit_testcase, name='testcase_change'),
    path('testcase/create/', views.edit_testcase, name='testcase_create'),
    path('testcase/create/<int:pk>/', views.edit_testcase, name='testcase_create'),

    #TestRun Views für die Forms
    path('testrun/<int:pk>/', views.edit_testrun, name='testrun_change'),
    path('testrun/create', views.edit_testrun, name='testrun_create'),
    path('testrun/create/<int:pk>/', views.edit_testrun, name='testrun_create'),

    path('testrun/run/<int:pk>/', views.testrun_run, name='testrun_run'),
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
]

