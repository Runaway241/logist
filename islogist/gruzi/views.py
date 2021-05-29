from django.shortcuts import render, redirect
from .forms import adduchastnikForm
from .models import Uchastnik, Zaiavka

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