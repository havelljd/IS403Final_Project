from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def betinfoView(request) :
    return HttpResponse('Hello Universe! This is the bet info view')

def readbetView(request) :
    return HttpResponse('Hello Universe! This is the read bet view')

def createbetView(request) :
    return HttpResponse('Hello Universe! This is the create bet view')

def updatebetView(request) :
    return HttpResponse('Hello Universe! This is the update bet view')

def deletebetView(request) :
    return HttpResponse('Hello Universe! This is the delete bet view')