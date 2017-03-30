# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from forum import views

urlpatterns = [
    url(r'^topic/$', views.TopicList.as_view()),
    url(r'^topic/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view()),
    url(r'^topic/(?P<tid>[0-9]+)/reply/$',
        views.ReplyList.as_view()),
    url(r'^topic/(?P<tid>[0-9]+)/reply/(?P<pk>[0-9]+)/$',
        views.ReplyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
