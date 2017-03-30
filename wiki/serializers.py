from rest_framework import serializers
from django.contrib.auth.admin import User
from wiki.models import Course, Article, ArticleModify


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        readonly = ('id', 'username', 'email')


class CourseSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Course
        fields = ('id', 'name', 'user')
        readonly = ('user', 'id')


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    course = CourseSerializer(required=False)

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'outline', 'rich_text',
            'create_time', 'modify_time', 'is_verify', 'user', 'course')
        readonly = (
            'id', 'create_time', 'modify_time', 'is_verify', 'user', 'course')


class ArticleModifySerializer(serializers.ModelSerializer):
    article = ArticleSerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = ArticleModify
        fields = (
            'id', 'title', 'outline', 'rich_text', 'create_time',
            'is_verify', 'article', 'user')
        readonly = ('id', 'create_time', 'is_verify', 'article', 'user')
