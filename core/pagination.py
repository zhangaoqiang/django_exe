# -*- coding: utf-8 -*-

from rest_framework import pagination
from rest_framework.views import Response


class LinkHeaderPagination(pagination.PageNumberPagination):
    page_size_query_param = 'per_page'
    max_page_size = 100

    def get_paginated_response(self, data):
        page = self.page.number
        last = self.page.paginator.num_pages
        next = last if last == page else page+1
        return Response({
            'data': data,
            'next': next,
            'page': page,
            'page_count': last,
            'data_count': self.page.paginator.count
        })
