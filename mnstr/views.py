# Create your views here.
from django.shortcuts import render
from mnstr.models import *
from django.template.loader import render_to_string
from django.utils import simplejson
from django.http import HttpResponse

fetch_comments = 5

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

def load_comments(request):
    topic = Topic.objects.get(pk=request.GET['topic_id'])
    lower_limit = int(request.GET['lower_limit'])
    comments_objs = Comment.objects.filter(topic = topic, parent=None).order_by("-votes")[lower_limit:lower_limit + fetch_comments]
    comments = []
    for comment in comments_objs:
        replies = Comment.objects.filter(parent=comment)
        comments.append({
            'comment': comment,
            'replies': replies
        })
    data = {
        'html': render_to_string('layouts/comments.html', { 'comments': comments }),
        'full': comments_objs.count() < fetch_comments
    }
    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')


def post_comment(request):
    comment = Comment(parent=None, topic = Topic.objects.get(pk=request.GET['topic_id']), username=request.GET['username'], content = request.GET['content'])
    comment.save()
    data = {
        'html': render_to_string('layouts/comment.html', { 'comment': comment, 'replies': [] }),
    }
    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')

