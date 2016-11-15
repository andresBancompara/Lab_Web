from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
    data = Cuenta.objects.get(id=1)
    response = JsonResponse(model_to_dict(data))
    return response
