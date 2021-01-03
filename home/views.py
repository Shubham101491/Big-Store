from django.shortcuts import render
from bigstore import settings
from home.models import Contact

from django.contrib import messages


def home(request):
    return render(request, 'home/index.html', {"BASE_URL": settings.BASE_URL})


def about(request):
    return render(request, 'home/about.html', {"BASE_URL": settings.BASE_URL})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']

        data_content = Contact(name=name, email=email, message=msg)
        data_content.save()

        messages.info(
            request, 'Thankyou for contact us, we will reply you soon')
    return render(request, 'home/contact.html', {"BASE_URL": settings.BASE_URL})
