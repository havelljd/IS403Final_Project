from django.urls import path
from .views import betinfoView, readbetView, createbetView, updatebetView, deletebetView

urlpatterns = [
    path("", betinfoView, name="betinfo"),    
    path("readbet/", readbetView, name="readbet"),
    path("createbet/", createbetView, name="createbet"),
    path("updatebet/", updatebetView, name="updatebet"),
    path("deletebet/", deletebetView, name="deletebet"),
]