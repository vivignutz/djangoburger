from django.http import HttpResponse
from django.shortcuts import render

# Create your views here:


def home(request):
    return render(request, 'djangoburger/home.html', {})


def details_product(request):
    return HttpResponse('This is the roduct details page')
