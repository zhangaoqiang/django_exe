# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_jwt.serializers import (
    jwt_payload_handler, jwt_encode_handler
)
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse

from user_info.serializers import UserRegisterSerializer, LoginSerializer


class SignUp(generics.CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = ()


class SignIn(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'detail': 'login successful.', 'token': token})

    def delete(self, request):
        logout(request)
        return Response({'detail': 'logout successful.'})
auth_jwt_token = SignIn.as_view()


class ActiveAccount(APIView):
    """
        用户注册邮箱激活
    """

    def get(self, request):
        username = request.GET.get('username')
        encrypt_username = request.GET.get('encrypt_username')
        if check_password(username, encrypt_username):
            User.objects.filter(username=username).update(is_active=True)
        return Response({'detail': 'active success'})


class UpdatePassword(APIView):
    """
        用户修改密码
    """

    def put(self, request):
        user = request.user
        origin_password = request.data['origin_password']
        new_password = request.data['new_password']
        if user.password == origin_password:
            user.set_password(new_password)
            user.save()
        else:
            return HttpResponse("please enter you origin password again!")


class UpdateProfile(generics.ListCreateAPIView):
    """
        编辑用户资料
    """
