from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



def index(request):
    data = {
        'title': 'Автомобильные перевозки грузов по России',

        }

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')