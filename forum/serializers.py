# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers
from forum.models import Topic, Reply
from wiki.models import Course


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        read_only_fields = ('id', 'username')


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(required=False)

    class Meta:

        model = Course
        fields = ('id', 'name', 'user')
        read_only_fields = ('user', 'id')


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(required=False, read_only=True)
    course = CourseSerializer(required=False, read_only=True)
    course_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Topic
        fields = (
            'id', 'title', 'content', 'create_time',
            'modify_time', 'user', 'course', 'course_id')
        read_only_fields = (
            'id', 'create_time',
            'modify_time', 'user', 'course')


class ReplySerializer(serializers.HyperlinkedModelSerializer):

    reply_topic = serializers.SerializerMethodField()
    user = UserSerializer(required=False, read_only=True)
    reply_self = serializers.SerializerMethodField()
    reply_self_id = serializers.CharField(required=True, write_only=True)

    def get_reply_self(self, obj):
        if obj.reply_self:
            return {
                'id': obj.reply_self.id,
                'user': obj.reply_self.user.username,
                'content': obj.reply_self.content
            }
        else:
            return None

    def get_reply_topic(self, obj):
        obj = obj.reply_topic
        if obj:
            return {
                'id': obj.id,
                'title': obj.title,
                'content': obj.content
            }
        else:
            return None

    class Meta:
        model = Reply
        fields = (
            'id', 'content', 'reply_topic', 'reply_self', 'reply_self_id',
            'create_time', 'modify_time', 'user')
        read_only_fields = ('id',  'create_time', 'modify_time', 'user')
