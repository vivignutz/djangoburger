from django.http import HttpResponse

# Create your views here:


def home(request):
    return HttpResponse('Hello Django!')

def details_product(request):
    return HttpResponse('Hello, you are in the product details page')