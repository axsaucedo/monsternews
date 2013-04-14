from django.db import models
from django.conf import settings

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=255)
    #time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
    
class News(models.Model):
    SOURCE_CHOICES = (
        ('BBC', 'BBC News'),
        ('GUARDIAN', 'The Guardian'),
        ('SKY', 'Sky News'),
        ('ITV', 'ITV News'),
        ('CH4', 'Channel 4'),
        ('INDEPENDENT', 'The Independant'),
        ('TIMES', 'The Times'),
        ('TELEGRAPH', 'The Telegraph'),
        )

    name = models.CharField(max_length=255)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    description = models.TextField()
    link = models.TextField()
    image_link = models.TextField()
    topic = models.ForeignKey(Topic)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    topic = models.ForeignKey(Topic)
    username = models.CharField(max_length=255, null=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children")
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username