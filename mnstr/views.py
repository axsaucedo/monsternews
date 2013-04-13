# Create your views here.
from django.shortcuts import render
from mnstr.models import *

def monsterHome(request):
    topics = Topic.objects.all()[:1]
    topic = topics[0]
    comments = Comment.objects.filter(topic = topic, parent=None).order_by("-votes")[:5]
    return render(request, "comments.html", {'comments': comments })