from django.shortcuts import render
from bigstore import settings

def water_beverages(request):
    return render(request, 'kitchen/kitchen.html', {"BASE_URL": settings.BASE_URL})
