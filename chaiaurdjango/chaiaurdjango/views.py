from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello, Welcome to Home Page")
    return render(request, 'website/index.html')

def About(request):
    # return HttpResponse("Hello , Welcome to About page")
    return render(request,  'website/about.html')

def Contact(request):
    return HttpResponse("Hello, Welcome to Contact Page")