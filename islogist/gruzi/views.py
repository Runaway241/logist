from django.shortcuts import render, redirect
from .forms import adduchastnikForm, addzaiavkarForm, adddogovorForm, addsprsotrForm, addactovipolnForm, addschetoplForm
from .models import Uchastnik, Zaiavka, Dogovor, SprSotr, SprModel, SprMarka, Trsredstvo, SprDolgn, SprTipgruza, \
    SprGruza, SprVidts, SprTovar, SprOrg, SprVidharts, Actovipoln, Schetopl


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

def actovipoln(request):
    gruzi = Actovipoln.objects.all()
    return render(request, 'gruzi/actovipoln.html', {'gruzi': gruzi})

def addactovipoln(request):
    error = ''
    if request.method == 'POST':
        form = addactovipolnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actovipoln')
        else:
            error = 'Форма неверна'
    form = addactovipolnForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addactovipoln.html', data)

def schetopl(request):
    gruzi = Schetopl.objects.all()
    return render(request, 'gruzi/schetopl.html', {'gruzi': gruzi})

def addschetopl(request):
    error = ''
    if request.method == 'POST':
        form = addschetoplForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schetopl')
        else:
            error = 'Форма неверна'
    form = addschetoplForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addschetopl.html', data)

'''Справочники'''
def sprmarka(request):
    gruzi = SprMarka.objects.all()
    return render(request, 'gruzi/sprmarka.html', {'gruzi': gruzi})
def sprmodel(request):
    gruzi = SprModel.objects.all()
    return render(request, 'gruzi/sprmodel.html', {'gruzi': gruzi})
def trsredstvo(request):
    gruzi = Trsredstvo.objects.all()
    return render(request, 'gruzi/trsredstvo.html', {'gruzi': gruzi})
def dolgn(request):
    gruzi = SprDolgn.objects.all()
    return render(request, 'gruzi/dolgn.html', {'gruzi': gruzi})
def sprtipgruza(request):
    gruzi = SprTipgruza.objects.all()
    return render(request, 'gruzi/sprtipgruza.html', {'gruzi': gruzi})
def sprgruza(request):
    gruzi = SprGruza.objects.all()
    return render(request, 'gruzi/sprgruza.html', {'gruzi': gruzi})
def sprvidts(request):
    gruzi = SprVidts.objects.all()
    return render(request, 'gruzi/sprvidts.html', {'gruzi': gruzi})
def sprtovar(request):
    gruzi = SprTovar.objects.all()
    return render(request, 'gruzi/sprtovar.html', {'gruzi': gruzi})
def sprorg(request):
    gruzi = SprOrg.objects.all()
    return render(request, 'gruzi/sprorg.html', {'gruzi': gruzi})
def sprvidharts(request):
    gruzi = SprVidharts.objects.all()
    return render(request, 'gruzi/sprvidharts.html', {'gruzi': gruzi})

