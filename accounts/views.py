from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import *
#from oauth2client import client, crypt
import json
from .models import *
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail


@login_required()
def logout_view(request):
    logout(request)
    # Redirect to a success page.


def autenticar_usuario(request):
    next = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        if request.POST.get('login'):
            username = request.POST['usuario']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    request.session['username'] = username
                    login(request, user)
                    return HttpResponseRedirect(next)
                else:
                    # Return a 'disabled account' error message
                    print ("Fail")

            else:
                # Return an 'invalid login' error message.
                print('invalid login')
        else:
            first_name = request.POST['nombre']
            last_name = request.POST['apellido']
            email = request.POST['email']
            password = request.POST['password']
            username = request.POST['username']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            #Email sending
            send_mail(
                'Registro Chromium' + first_name + ' ' + last_name,
                'Gracias ' + first_name + ' por registrar tus datos.Ya puedes acceder con tus datos a nuestra plataforma con tu usuario: ' + username,
                'andresvillavicencio92@gmail.com',
                [email],
                fail_silently=False,
            )

            return render(request, 'log_in.html')
    else:
        return render(request, 'log_in.html')
