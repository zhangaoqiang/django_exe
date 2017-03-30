# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from wiki.models import Course


class VisitLog(models.Model):
    '''
        用户的访问日志
    '''
    user = models.ForeignKey(User, verbose_name="用户")
    user_agent = models.CharField(max_length=30, verbose_name="使用浏览器")
    user_origin = models.CharField(max_length=300, verbose_name="用户初始的URL")
    user_refer = models.CharField(max_length=300, verbose_name="用户重定向的URL")
    visit_time = models.DateTimeField(null=True, verbose_name="用户访问时间")
    visit_ip = models.GenericIPAddressField(verbose_name="用户访问ip")


class LearnProcess(models.Model):
    '''
        用户的学习进度日志
    '''
    user = models.ForeignKey(User, verbose_name="用户")
    course = models.ForeignKey(Course, verbose_name="课程")
    process = models.FloatField(max_length=5, verbose_name="学习进度")
    learning_time = models.FloatField(max_length=5, verbose_name="学习时长")