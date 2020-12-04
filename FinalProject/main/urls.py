from django.urls import path
from .views import  mainlogoutpageView, gameDisplayView, deletePageView, updatePageView, addPageView, indexPageView, specificgameDisplayView

urlpatterns = [  
    path("specificgamedisplay/", specificgameDisplayView, name= "specificgame"),
    path("mainlogoutpage/", mainlogoutpageView, name="mainlogout"),
    path("gamedisplay/", gameDisplayView, name="gamedisplay"),  
    path("deletegame/", deletePageView, name="deletegame"),
    path("updategame/", updatePageView, name="updategame"),
    path("addgame/", addPageView, name="addgame"),
    path("", indexPageView, name="index"),
]
