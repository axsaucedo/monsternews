# Create your views here.
from django.shortcuts import render
from mnstr.models import *

def monsterHome(request):
    topics = Topic.objects.all()[:1]
    topic = topics[0]
    comments = []
    comments_objs = Comment.objects.filter(topic = topic, parent=None).order_by("-votes")[:5]
    for comment in comments_objs:
        replies = Comment.objects.filter(parent=comment)
        comments.append({
            'comment': comment,
            'replies': replies
        })
    return render(request, "comments.html", {'comments': comments })

def load_comments(request):
    topic = Topic.objects.get(pk=request.POST.topic_id)

def home(request):
    allTopics = Topic.objects.all()[:5]

    topics = []
    for topic in allTopics:
        #Retreiving News objects from database related to topic
        news_objs =  News.objects.filter(topic=topic)

        #retreiving Comments object from database related to topic
        comments_objs = Comment.objects.filter(topic=topic, parent=None).order_by("-votes")[:5]
        comments = [] #This object will retain Comments and Replies

        #Splitting comments and replies
        for comment in comments_objs:
            replies = Comment.objects.filter(parent=comment)
            comments.append({
                'comment': comment,
                'replies': replies
            })

        topics.append({ 'topic' : topic ,'news': news_objs, 'comments' : comments})

    return render(request, "main.html", { 'topics' : topics })