# Create your views here.
from django.shortcuts import render

def main(request):
    return render(request, "main.html")
