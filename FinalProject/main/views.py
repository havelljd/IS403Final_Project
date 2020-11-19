from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mainpageView(request):
    return render(request, 'betpages/index.html')

def mainlogoutpageView(request):
    return HttpResponse('This is the logout page!!')