from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gameinfoView(request) :
    return render(request, 'gameinfo/gameinfo.html')

def readgameView(request) :
    return render(request, 'gameinfo/readgame.html')

def creategameView(request) :
    return render(request, 'gameinfo/creategame.html')

def updategameView(request) :
    return render(request, 'gameinfo/updategame.html')

def deletegameView(request) :
    return render(request, 'gameinfo/deletegame.html')
