from django.urls import path
from .views import mainpageView, mainlogoutpageView

urlpatterns = [
    
    path("mainpage/", mainpageView, name="main"),    
    path("mainlogoutpage/", mainlogoutpageView, name="main"),    
]
