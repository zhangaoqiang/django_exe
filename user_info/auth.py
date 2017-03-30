# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from rest_framework_jwt.authentication import (
    JSONWebTokenAuthentication as _JSONWebTokenAuthentication
)

logger = logging.getLogger(__name__)


class APIBackend(ModelBackend):

    def authenticate(self, username=None, password=None,
                     **kwargs):
        if not all([username, password]):
            return None
        try:
            user = User.objects.get(
                username=username, is_active=True
            )
        except User.DoesNotExist:
            try:
                user = User.objects.get(
                    email=username, is_active=True
                )
            except User.DoesNotExist:
                return None

        if not user.check_password(password):
            return None
        if user.check_password(password):
            return user


class JSONWebTokenAuthentication(_JSONWebTokenAuthentication):

    def get_jwt_value(self, request):
        if settings.DEBUG:  # DEBUG 模式下支持在 URL 中使用 token 参数
            from rest_framework_jwt.settings import api_settings
            auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX
            token = getattr(request, 'query_params', request.GET).get('token')
            if token:
                request.META.setdefault(
                    'HTTP_AUTHORIZATION', '%s %s' % (auth_header_prefix, token)
                )

        return super(JSONWebTokenAuthentication, self).get_jwt_value(request)
