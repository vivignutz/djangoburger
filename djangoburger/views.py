from django.http import HttpResponse

# Create your views here:


def home(request):
    return HttpResponse('Hello Django!')


def details_product(request):
    return HttpResponse('This is the roduct details page')
