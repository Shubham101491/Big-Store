from django.shortcuts import render
from bigstore import settings

def shipping(request):
    return render(request, 'other/shipping.html', {"BASE_URL": settings.BASE_URL})

def offer(request):
    return render(request, 'other/offer.html', {"BASE_URL": settings.BASE_URL})

def wishlist(request):
    return render(request, 'other/wishlist.html', {"BASE_URL": settings.BASE_URL})

def single(request):
    return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL})

def terms(request):
    return render(request, 'other/terms.html', {"BASE_URL": settings.BASE_URL})

def faqs(request):
    return render(request, 'other/faqs.html', {"BASE_URL": settings.BASE_URL})

