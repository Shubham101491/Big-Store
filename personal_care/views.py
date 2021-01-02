from django.shortcuts import render
from bigstore import settings


def care(request):
    return render(request, 'pcare/care.html', {"BASE_URL": settings.BASE_URL})
