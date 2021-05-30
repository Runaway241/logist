from django.shortcuts import render, redirect
from .forms import adduchastnikForm, addzaiavkarForm, adddogovorForm, addsprsotrForm
from .models import Uchastnik, Zaiavka, Dogovor, SprSotr

def uchastnik(request):
    gruzi = Uchastnik.objects.all()
    return render(request, 'gruzi/uchastnik.html', {'gruzi': gruzi})

def adduchastnik(request):
    error = ''
    if request.method == 'POST':
        form = adduchastnikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uchastnik')
        else:
            error = 'Форма неверна'
    form = adduchastnikForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/adduchastnik.html', data)

def zaiavka(request):
    gruzi = Zaiavka.objects.all()
    return render(request, 'gruzi/zaiavka.html', {'gruzi': gruzi})

def addzaiavka(request):
    error = ''
    if request.method == 'POST':
        form = addzaiavkarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zaiavka')
        else:
            error = 'Форма неверна'
    form = addzaiavkarForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addzaiavka.html', data)

def dogovor(request):
    gruzi = Dogovor.objects.all()
    return render(request, 'gruzi/dogovor.html', {'gruzi': gruzi})

def adddogovor(request):
    error = ''
    if request.method == 'POST':
        form = adddogovorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dogovor')
        else:
            error = 'Форма неверна'
    form = adddogovorForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/adddogovor.html', data)

def sprsotr(request):
    gruzi = SprSotr.objects.all()
    return render(request, 'gruzi/sprsotr.html', {'gruzi': gruzi})

def addsprsotr(request):
    error = ''
    if request.method == 'POST':
        form = addsprsotrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprsotr')
        else:
            error = 'Форма неверна'
    form = addsprsotrForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addsprsotr.html', data)
