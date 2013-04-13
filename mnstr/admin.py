from django.contrib import admin
from mnstr.models import Topic, News, Comment

class NewsInline(admin.StackedInline):
    model = News
    extra = 8

class TopicAdmin(admin.ModelAdmin):

    inlines = [NewsInline]

admin.site.register(Topic, TopicAdmin)
admin.site.register(News)
admin.site.register(Comment)
