from django.shortcuts import render
from bigstore import settings


def home(request):
    return render(request, 'home/index.html', {"BASE_URL": settings.BASE_URL})


def about(request):
    return render(request, 'home/about.html', {"BASE_URL": settings.BASE_URL})


def contact(request):
    return render(request, 'home/contact.html', {"BASE_URL": settings.BASE_URL})
