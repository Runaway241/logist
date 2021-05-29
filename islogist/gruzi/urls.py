from django.urls import path
from . import views

urlpatterns = [
    path('uchastnik', views.uchastnik, name='uchastnik'),
    path('adduchastnik', views.adduchastnik, name='adduchastnik')
    ]