from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def service(request):
    return HttpResponse('Hello, this is the services page')
