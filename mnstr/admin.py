from django.contrib import admin
from mnstr.models import Topic, News, Comment

class NewsAdmin(admin.ModelAdmin):
    fields = ['name', 'source', 'link', 'image_link', 'topic']

    list_display = ['name', 'source', 'link', 'image_link', 'topic']
#    ordering = ('zwitchlinkid',)

#class Topic(models.Model):
#    name = models.CharField(max_length=255)
#
#class News(models.Model):
#    name = models.CharField(max_length=255)
#    source = models.CharField(max_length=255)
#    link = models.TextField()
#    image_link = models.TextField()
#    topic = models.ForeignKey(Topic)
#
#class Comment(models.Model):
#    topic = models.ForeignKey(Topic)
#    username = models.CharField(max_length=255, null=True)
#    content = models.CharField(max_length=255)
#    time = models.DateTimeField(auto_now_add=True)
#    parent = models.ForeignKey("self", null=True, related_name="children")
#    votes = models.IntegerField(default=0)

admin.site.register(Topic)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
