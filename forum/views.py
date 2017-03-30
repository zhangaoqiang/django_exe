# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from forum.models import Topic, Reply
from forum.serializers import TopicSerializer, ReplySerializer
from rest_framework import generics


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        user = User.objects.get(pk=1)
        serializer.save(
            user=user
        )


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def perform_create(self, serializer):
        user = User.objects.get(pk=1)
        topic = Topic.objects.get(pk=self.kwargs['tid'])
        serializer.save(
            user=user,
            reply_topic=topic
        )

    def get_queryset(self):
        topic_id = self.kwargs['tid']
        return self.queryset.filter(reply_topic__id=topic_id)


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
