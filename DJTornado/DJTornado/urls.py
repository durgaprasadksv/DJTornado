from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^grumblr/', include('grumblr.urls')),
    url(r'^$', 'grumblr.views.home'),
)
