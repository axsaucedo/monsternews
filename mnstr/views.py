# Create your views here.
from django.shortcuts import render
from mnstr.models import *
from django.template.loader import render_to_string
from django.utils import simplejson
from django.http import HttpResponse

fetch_comments = 6
fecth_topics = 1
line_news = 4

def get_topics_list(allTopics):
    topics = []
    for topic in allTopics:
        #Retreiving News objects from database related to topic
        news_objs =  News.objects.filter(topic=topic)
        
        news_groups = []

        for n in news_objs:
            n.source = "static/media/mainimg/" + n.source + ".png"
        
        news_count = news_objs.count()
        slice_pos = 0
        while slice_pos < news_count:
            news_groups.append(news_objs[slice_pos:slice_pos + line_news])
            slice_pos += line_news


        #retreiving Comments object from database related to topic
        comments_objs = Comment.objects.filter(topic=topic, parent=None).order_by("-votes")[:fetch_comments]
        comments = [] #This object will retain Comments and Replies

        #Splitting comments and replies
        for comment in comments_objs:
            replies = Comment.objects.filter(parent=comment)
            comments.append({
                'comment': comment,
                'replies': replies
            })

        topics.append({ 'topic' : topic ,'news_groups': news_groups, 'comments' : comments})
        
    return topics

def home(request):
    return render(request, "main.html", { 'topics' : get_topics_list(Topic.objects.all()[:fecth_topics]) })

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
    comment = Comment(parent=None, topic = Topic.objects.get(pk=request.POST['topic_id']), username=request.POST['username'], content = request.POST['content'])
    comment.save()
    data = {
        'html': render_to_string('layouts/comment.html', { 'comment': comment, 'replies': [] }),
    }
    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')

def post_reply(request):
    parent_comment = Comment.objects.get(pk=request.POST['comment_id'])
    comment = Comment(parent=parent_comment, topic = parent_comment.topic, username=request.POST['username'], content = request.POST['content'])
    comment.save()
    data = {
        'html': render_to_string('layouts/reply.html', { 'comment': comment, "display": True }),
    }
    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')

def vote_comment(request):
    comment = Comment.objects.get(pk=request.POST['comment_id'])
    comment.votes += int(request.POST['delta'])
    comment.save()
    data = {
        'votes_count':  comment.votes,
        'pos': -1 
    }
    if comment.parent == None:
        data['pos'] = Comment.objects.filter(votes__gte = comment.votes, parent=None, topic=comment.topic).count() - 1
    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')

def source_click(request):
    news = News.objects.get(pk=request.POST['source_id'])
    news.views += 1
    news.save()
    return HttpResponse()

def load_topics(request):
    lower_limit = int(request.GET['lower_limit'])
    allTopics = Topic.objects.all()[lower_limit:lower_limit + fecth_topics]
    data = {
        'html': render_to_string('layouts/topics.html', { 'topics': get_topics_list(allTopics) }),
        'full': allTopics.count() < fecth_topics
    }
    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')
