from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # url(r'^monsternews/', include('monsternews.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'mnstr.views.home', name='home'),
    url(r'^load_comments/$', 'mnstr.views.load_comments', name='load_comments'),
    url(r'^post_comment/$', 'mnstr.views.post_comment', name='post_comment'),
    url(r'^post_reply/$', 'mnstr.views.post_reply', name='post_reply'),
     url(r'^vote_comment/$', 'mnstr.views.vote_comment', name='vote_comment'),
    url(r'^admin/', include(admin.site.urls)),
)
