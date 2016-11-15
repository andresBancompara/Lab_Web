from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import *
from oauth2client import client, crypt
import json
from .models import *
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

@login_required()
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def autenticar_usuario(request):
    next = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                # Return a 'disabled account' error message
                print ("Fail")

        else:
            # Return an 'invalid login' error message.
            print('invalid login')

    else:
        return render(request, 'log_in.html')