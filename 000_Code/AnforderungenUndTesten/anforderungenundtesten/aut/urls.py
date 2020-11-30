from django.urls import path, include, re_path

from . import  views

#auf die Namen aufpassen ob die irgendwo bbenutzt werden
app_name = 'aut'
urlpatterns = [
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

]

