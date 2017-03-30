# -*- coding: utf-8 -*-

from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from wiki.serializers import ArticleSerializer, ArticleModifySerializer
from wiki.models import Article, ArticleModify


class WikiList(APIView):
    """
    according to course_id find wiki
    """

    def get_object(self, pk):

        try:
            return Article.objects.filter(course__id=pk)
        except Article.DoesnotExist:
            raise Http404

    def get(self, request, pk):

        articleList = self.get_object(pk)
        serializer = ArticleSerializer(articleList, many=True)
        return Response(serializer.data)


class Wiki(APIView):

    def get_object(self, pk):

        try:
            return Article.objects.get(id=pk)
        except Article.DoesnotExist:
            raise Http404

    def get(self, request, pk):

        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class preArticle(APIView):
    def get_object(self, pk):

        try:
            return ArticleModify.objects.filter(article__id=pk)
        except ArticleModify.DoesnotExist:
            raise Http404

    def get(self, request, pk):

        ArticleModify = self.get_object(pk)
        serializer = ArticleModifySerializer(ArticleModify, many=True)
        return Response(serializer.data)
