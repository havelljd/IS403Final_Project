from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gameinfoView(request) :
    return HttpResponse('Hello Universe! This is the game info view')

def readgameView(request) :
    return HttpResponse('Hello Universe! This is the read game view')

def creategameView(request) :
    return HttpResponse('Hello Universe! This is the create game view')

def updategameView(request) :
    return HttpResponse('Hello Universe! This is the update game view')

def deletegameView(request) :
    return HttpResponse('Hello Universe! This is the delete game view')