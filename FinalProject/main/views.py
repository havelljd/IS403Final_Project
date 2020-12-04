from django.shortcuts import render
from .models import game
from django.views.decorators.csrf import csrf_protect


# Create your views here.
from django.http import HttpResponse

def mainpageView(request):
    
    data = game.objects.all()

    context = {
        "games": data
    }
    return render(request, 'betpages/test.html', context)

def specificgameDisplayView(request):
    iGameID=request.GET['game_id_display']
    data=game.objects.filter(id=iGameID)

    if data.count() > 0:
        context = {
            "our_games" : data
        }
        return render(request, 'betpages/displaygame.html', context)
    else:
        return HttpResponse("Not found")

def mainlogoutpageView(request):
    return render(request, 'betpages/logout.html')


def gameDisplayView(request):

    data=game.objects.all()
    if data.count() > 0:
        context = {
            "our_games" : data
        }
        return render(request, 'betpages/displaygame.html', context)
    else:
        return HttpResponse("Not found")

def mainlogoutpageView(request):
    return render(request, 'betpages/logout.html')

    
def deletePageView(request):
    iGameIdDelete = request.GET['game_id_delete']
    game.objects.filter(id=iGameIdDelete).delete()
    data = game.objects.all()
    if data.count() == 0:
        context = {
            "our_games" : data
        }
        return (request, 'betpages/deletegame.html', context)
    else:
        return HttpResponse(str(iGameIdDelete) + " was deleted")

def updatePageView(request):
    
    iGameID = request.POST['update_game_id']
    HomeTeam = request.POST['home_team']
    AwayTeam = request.POST['away_team']
    DatePlayed = request.POST['date_played']
    HomeTeamScore = request.POST['home_team_score']
    AwayTeamScore = request.POST['away_team_score']
    game.objects.filter(id=iGameID).update(Home_Team=HomeTeam, Away_Team = AwayTeam, date_played = DatePlayed, home_team_score = HomeTeamScore, away_team_score = AwayTeamScore)
    data = game.objects.filter(id=iGameID)

    context = {
        "updated_game": data
    }

    return render(request, 'betpages/displayupdategame.html', context)

def addPageView(request):
    new_game = game()

    new_game.Home_Team = request.POST.get('home_team')
    new_game.Away_Team = request.POST.get('away_team')
    new_game.date_played = request.POST.get('date_played')
    new_game.home_team_score = request.POST.get('home_team_score')
    new_game.away_team_score = request.POST.get('away_team_score')
    new_game.save()

    data = game.objects.all()

    context = {
        "our_games" : data
    }
    return render(request, 'betpages/addgame.html', context)



def indexPageView(request):
    return render(request, 'betpages/index.html')
