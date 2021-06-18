from django.shortcuts import render, redirect
from .forms import adduchastnikForm, addzaiavkarForm, adddogovorForm, addsprsotrForm, addactovipolnForm, \
    addschetoplForm, addschetfactForm, addputlistForm, addttnForm, addtrsredstvoForm, addmodelForm, addmarkaForm, \
    adddolgnForm, addtipgruzaForm, addorgForm, addotchpodogForm, addotchdoglogForm
from .models import Uchastnik, Zaiavka, Dogovor, SprSotr, SprModel, SprMarka, Trsredstvo, SprDolgn, SprTipgruza, \
    SprGruza, SprVidts, SprTovar, SprOrg, SprVidharts, Actovipoln, Schetopl, Schetfact, Putlist, Ttn, Otchpodog, \
    Otchdoglog


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


def schetfact(request):
    gruzi = Schetfact.objects.all()
    return render(request, 'gruzi/schetfact.html', {'gruzi': gruzi})
def addschetfact(request):
    error = ''
    if request.method == 'POST':
        form = addschetfactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schetfact')
        else:
            error = 'Форма неверна'
    form = addschetfactForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addschetfact.html', data)

def putlist(request):
    gruzi = Putlist.objects.all()
    return render(request, 'gruzi/putlist.html', {'gruzi': gruzi})
def addputlist(request):
    error = ''
    if request.method == 'POST':
        form = addputlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('putlist')
        else:
            error = 'Форма неверна'
    form = addputlistForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addputlist.html', data)

def ttn(request):
    gruzi = Ttn.objects.all()
    return render(request, 'gruzi/ttn.html', {'gruzi': gruzi})
def addttn(request):
    error = ''
    if request.method == 'POST':
        form = addttnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ttn')
        else:
            error = 'Форма неверна'
    form = addttnForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addttn.html', data)

'''Справочники'''
def sprmarka(request):
    gruzi = SprMarka.objects.all()
    return render(request, 'gruzi/sprmarka.html', {'gruzi': gruzi})
def addmarka(request):
    error = ''
    if request.method == 'POST':
        form = addmarkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprmarka')
        else:
            error = 'Форма неверна'
    form = addmarkaForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addmarka.html', data)

def sprmodel(request):
    gruzi = SprModel.objects.all()
    return render(request, 'gruzi/sprmodel.html', {'gruzi': gruzi})
def addmodel(request):
    error = ''
    if request.method == 'POST':
        form = addmodelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model')
        else:
            error = 'Форма неверна'
    form = addmodelForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addmodel.html', data)

def trsredstvo(request):
    gruzi = Trsredstvo.objects.all()
    return render(request, 'gruzi/trsredstvo.html', {'gruzi': gruzi})
def addtrsredstvo(request):
    error = ''
    if request.method == 'POST':
        form = addtrsredstvoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trsredstvo')
        else:
            error = 'Форма неверна'
    form = addtrsredstvoForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addtrsredstvo.html', data)

def dolgn(request):
    gruzi = SprDolgn.objects.all()
    return render(request, 'gruzi/dolgn.html', {'gruzi': gruzi})
def adddolgn(request):
    error = ''
    if request.method == 'POST':
        form = adddolgnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dolgn')
        else:
            error = 'Форма неверна'
    form = adddolgnForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/adddolgn.html', data)

def sprtipgruza(request):
    gruzi = SprTipgruza.objects.all()
    return render(request, 'gruzi/sprtipgruza.html', {'gruzi': gruzi})
def addtipgruza(request):
    error = ''
    if request.method == 'POST':
        form = addtipgruzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprtipgruza')
        else:
            error = 'Форма неверна'
    form = addtipgruzaForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addtipgruza.html', data)

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
def addorg(request):
    error = ''
    if request.method == 'POST':
        form = addorgForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprorg')
        else:
            error = 'Форма неверна'
    form = addorgForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addorg.html', data)

def sprvidharts(request):
    gruzi = SprVidharts.objects.all()
    return render(request, 'gruzi/sprvidharts.html', {'gruzi': gruzi})

def otchpodog(request):
    gruzi = Otchpodog.objects.all()
    return render(request, 'gruzi/otchpodog.html', {'gruzi': gruzi})
def addotchpodog(request):
    error = ''
    if request.method == 'POST':
        form = addotchpodogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('otchpodog')
        else:
            error = 'Форма неверна'
    form = addotchpodogForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addotchpodog.html', data)

def otchdoglog(request):
    gruzi = Otchdoglog.objects.all()
    return render(request, 'gruzi/otchdoglog.html', {'gruzi': gruzi})
def addotchdoglog(request):
    error = ''
    if request.method == 'POST':
        form = addotchdoglogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('otchdoglog')
        else:
            error = 'Форма неверна'
    form = addotchdoglogForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'gruzi/addotchdoglog.html', data)