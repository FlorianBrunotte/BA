from django.urls import path, include

from . import  views

urlpatterns = [
    path('', views.index, name ='index'), #hier steht nix ist aber unter /aut/ weil das in dem Haupt url File steht
    path('req/', views.RequirementView.as_view(), name='req'), #für einzelne Anforderungen
    path('req/<int:pk>', views.RequirementView.as_view(), name='req_detail'),  #Details

]