# Create your views here.
from django.shortcuts import render
from mnstr.models import *

def monsterHome(request):
    topics = Topic.objects.all()[:1]
    comments = Comment.objects.filter(topic_id = topics[0].id)
    return render(request, "main.html")


def home(request):
