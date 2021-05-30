from django.urls import path
from . import views

urlpatterns = [
    path('uchastnik', views.uchastnik, name='uchastnik'),
    path('adduchastnik', views.adduchastnik, name='adduchastnik'),
    path('zaiavka', views.zaiavka, name='zaiavka'),
    path('addzaiavka', views.addzaiavka, name='addzaiavka'),
    path('dogovor', views.dogovor, name='dogovor'),
    path('adddogovor', views.adddogovor, name='adddogovor')
    ]