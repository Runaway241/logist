from django.urls import path
from . import views

urlpatterns = [
    path('uchastnik', views.uchastnik, name='uchastnik'),
    path('adduchastnik', views.adduchastnik, name='adduchastnik'),
    path('zaiavka', views.zaiavka, name='zaiavka'),
    path('addzaiavka', views.addzaiavka, name='addzaiavka'),
    path('dogovor', views.dogovor, name='dogovor'),
    path('adddogovor', views.adddogovor, name='adddogovor'),
    path('sprsotr', views.sprsotr, name='sprsotr'),
    path('addsprsotr', views.addsprsotr, name='addsprsotr'),

    path('sprmarka', views.sprmarka, name='sprmarka'),
    path('sprmodel', views.sprmodel, name='sprmodel'),
    path('trsredstvo', views.trsredstvo, name='trsredstvo'),
    path('dolgn', views.dolgn, name='dolgn'),
    path('sprtipgruza', views.sprtipgruza, name='sprtipgruza'),
    path('sprgruza', views.sprgruza, name='sprgruza'),
    path('sprvidts', views.sprvidts, name='sprvidts'),
    path('sprtovar', views.sprtovar, name='sprtovar'),
    path('sprorg', views.sprorg, name='sprorg'),
    path('sprvidharts', views.sprvidharts, name='sprvidharts'),
    ]