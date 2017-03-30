# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.admin import User


class UserEmail(models.Model):
    """
        用户注册邮件链接类
    """
    user = models.ForeignKey(User, verbose_name="用户")
    content = models.TextField(verbose_name="邮件内容")


class UserProfile(models.Model):
    """
      用户基础信息
    """
    user = models.ForeignKey(User, verbose_name="用户")
    real_name = models.CharField(max_length=30, verbose_name="真实姓名")
    photo = models.CharField(max_length=30, verbose_name="照片")
    location = models.CharField(max_length=30, verbose_name="所在地")
    interest = models.CharField(max_length=30, verbose_name="兴趣")
    sex = models.BooleanField(verbose_name="性别")
    birthday = models.DateField(null=True, verbose_name="生日")
    introduce = models.TextField(verbose_name="个人简介")


class Education(models.Model):
    """
        教育信息类
    """
    organization = models.CharField(max_length=50, verbose_name="教育机构名称")
    start_date = models.DateField(null=True, verbose_name="开始日期")
    end_date = models.DateField(null=True, verbose_name="结束日期")
    major = models.CharField(max_length=20, verbose_name="主修专业")
    degree = models.CharField(max_length=20, verbose_name="所获学位")


class UserEducation(models.Model):
    """
    用户教育信息关联类
    """
    user = models.ForeignKey(User, verbose_name="关联用户")
    edu = models.ForeignKey(Education, verbose_name="关联教育信息")








