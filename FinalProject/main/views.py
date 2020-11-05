from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mainpageView(request):
    return HttpResponse('This is the login page!!')

def mainlogoutpageView(request):
    return HttpResponse('This is the logout page!!')