from django.urls import path, include

from . import  views

urlpatterns = [
    path('', views.index, name ='index'), #hier steht nix ist aber unter /polls/ weil das in dem Haupt url File steht
]