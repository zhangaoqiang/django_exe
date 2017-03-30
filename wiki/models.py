# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.admin import User
from ckeditor.fields import RichTextField
from django.contrib import admin


class Course(models.Model):

    # 自增长
    id = models.AutoField(primary_key=True)

    # 课程名称
    name = models.CharField(max_length=30)

    # 关联user表
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.CharField(max_length=100)
    # #富文本信息
    rich_text = RichTextField('正文')
    # 文章概要
    outline = models.CharField(max_length=30, blank=True)
    # 文章创建时间（一次产生）
    create_time = models.DateTimeField(auto_now_add=True)
    # 最后修改的时间
    modify_time = models.DateTimeField(auto_now=True)
    # 是否被通过审核
    is_verify = models.BooleanField()
    # 关联user表
    user = models.ForeignKey(User)
    # 关联course表
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.title


class ArticleModify(models.Model):
    id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.CharField(max_length=100)
    # 富文本信息
    rich_text = RichTextField('正文')
    # 文章概要
    outline = models.CharField(max_length=30, blank=True)
    # 文章创建时间（一次产生）
    create_time = models.DateTimeField(auto_now_add=True)
    # 是否被通过审核
    is_verify = models.BooleanField()
    # 关联user表
    user = models.ForeignKey(User)
    # 关联Article表
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.title


class ArticleHistory(models.Model):
    id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.CharField(max_length=100)
    # 富文本信息
    rich_text = RichTextField('正文')
    # 文章概要
    outline = models.CharField(max_length=30, blank=True)
    # 文章创建时间（一次产生）
    create_time = models.DateTimeField(auto_now_add=True)
    # 版本号
    version_num = models.CharField(max_length=30, blank=True)
    # 关联user表
    user = models.ForeignKey(User)
    # 关联Article表
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.title

# class ArticleHistoryForm():
#     # 文章标题
#     title = forms.CharField(max_length=100)
#     # #富文本信息
#     rich_text = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Article
#         fields = "__all__"

admin.site.register(Course)
admin.site.register(Article)
admin.site.register(ArticleHistory)
admin.site.register(ArticleModify)
