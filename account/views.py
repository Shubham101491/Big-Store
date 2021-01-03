from django.shortcuts import render
from bigstore import settings
from account.forms import RegisterForm

from django.contrib import messages


def login(request):
    return render(request, 'account/login.html', {"BASE_URL": settings.BASE_URL})


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)

        if register_form.is_valid():
            user = register_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(register_form.errors)
    else:
        register_form = RegisterForm()

        messages.info(
            request, 'Thankyou, You have been Registered, Feel Free To Shop')
    return render(request, 'account/register.html', {"BASE_URL": settings.BASE_URL, 'register_form': register_form})
