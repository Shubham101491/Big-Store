from django.shortcuts import render
from bigstore import settings


def login(request):
    return render(request, 'account/login.html', {"BASE_URL": settings.BASE_URL})


def register(request):
    return render(request, 'account/register.html', {"BASE_URL": settings.BASE_URL})
