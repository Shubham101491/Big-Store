from django.shortcuts import render
from bigstore import settings


def hold(request):
    return render(request, 'household/hold.html', {"BASE_URL": settings.BASE_URL})
