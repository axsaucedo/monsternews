# Create your views here.
from django.shortcuts import render

def monsterHome(request):
    return render(request, "main.html")