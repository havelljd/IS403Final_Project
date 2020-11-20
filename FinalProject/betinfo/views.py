from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def betinfoView(request) :
    return render(request, 'betinfo/betinfo.html')

def readbetView(request) :
    return render(request, 'betinfo/readbet.html')

def createbetView(request) :
    return render(request, 'betinfo/createbet.html')

def updatebetView(request) :
    return render(request, 'betinfo/updatebet.html')

def deletebetView(request) :
    return render(request, 'betinfo/deletebet.html')