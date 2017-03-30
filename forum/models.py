# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from wiki.models import Course
from django.contrib import admin


class Topic(models.Model):

    '''
    发帖数据表
    '''

    user = models.ForeignKey(User, verbose_name="发帖人")
    title = models.CharField(
        max_length=100, blank=True, default='', verbose_name="帖子标题")
    course = models.ForeignKey(Course,  verbose_name="目标课程")
    content = RichTextField(verbose_name="帖子内容")
    modify_time = models.DateTimeField(
        auto_now=True, null=True, verbose_name="修改时间")
    create_time = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="创建时间")

    def __unicode__(self):
        return '%s' % self.title


class Reply(models.Model):

    '''
    回帖数据表
    '''

    user = models.ForeignKey(User, verbose_name="发帖人")
    content = RichTextField(verbose_name="回帖内容")
    reply_topic = models.ForeignKey(
        Topic, verbose_name="回复帖子", null=True, blank=True)
    reply_self = models.ForeignKey(
        'self', verbose_name='回复回帖', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True,
                                       verbose_name="回帖时间")
    modify_time = models.DateTimeField(auto_now=True, null=True,
                                       verbose_name="修改时间")


admin.site.register(Topic)
admin.site.register(Reply)
