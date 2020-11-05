from django.urls import path
from .views import gameinfoView, readgameView, creategameView, updategameView, deletegameView

urlpatterns = [
    path("", gameinfoView, name="gameinfo"),    
    path("readgame/", readgameView, name="readgame"),
    path("creategame/", creategameView, name="creategame"),
    path("updategame/", updategameView, name="updategame"),
    path("deletegame/", deletegameView, name="deletegame"),
]