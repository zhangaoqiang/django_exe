# -*- coding: utf-8 -*-
from django.conf.urls import url
from wiki import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(
        r'^course/(?P<pk>[0-9]+)/article/$',
        views.WikiList.as_view()),  # 根据课程id获取所有wiki
    # url(r'^course/<:cid>/article/',
    #  views.SignIn.as_view()),# 根据课程id获取所有wiki
    url(
        r'^article/(?P<pk>[0-9]+)/$',
        views.Wiki.as_view()),  # 根据文章wikiID获取wiki
    # url(r'^course/article/<:aid>/',
    # views.SignUp.as_view()),# 根据文章wikiID获取wiki
    # url(r'^add', views.SignIn.as_view()),# 教师新建wiki(只能是教师做的事情)
    # url(r'^modify_article/<:wid>',
    # views.SignUp.as_view()),# 保存提交wiki的修改
    # url(r'^pre_article/<:wid>',
    # views.SignIn.as_view()),# 通过wikiId获取该wiki下的待审核的wiki
    url(
        r'^pre_article/(?P<pk>[0-9]+)/$',
        views.preArticle.as_view()),  # url(r'^pass/<:wid>#wid:wiki_id',
    # views.SignUp.as_view()),# 教师审核提交的wiki
    # url(r'^versions/<:wid>#wid:wiki_id',
    # views.SignIn.as_view()),# 教师获取wiki版本信息列表
    # url(r'^<:wid>/merge/', views.SignUp.as_view()),# 教师合并wiki版本
]

urlpatterns = format_suffix_patterns(urlpatterns)
