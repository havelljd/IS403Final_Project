from django.urls import path
from .views import mainpageView, mainlogoutpageView

urlpatterns = [
    
    path("", mainpageView, name="main"),    
    path("mainlogoutpage/", mainlogoutpageView, name="mainlogout"),    
]
