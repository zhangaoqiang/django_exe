# -*- coding: utf-8 -*-
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth.admin import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from user_info.models import UserProfile, UserEmail
# from user_logs.models import VisitLog
from web.local_settings import MY_HOST


# class CreateUserSerializer(serializers.ModelSerializer):
#     """
#         用户信息的序列化
#     """
#     password = serializers.CharField(
# min_length=4, max_length=12, write_only=True,required=True)
#     username = serializers.CharField(
# min_length=6, max_length=12, required=True)
#     email = serializers.CharField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('email', 'username', 'password')
#         # extra_kwargs = {'password': {'write_only': True}}
#
#     # 用户的邮箱验证
#     def validate_email(self, value):
#         email = value.strip()
#         check_email = User.objects.filter(email=email)
#         if check_email:
#             raise serializers.ValidationError(u"邮箱已经被注册了")
#         else:
#             return value
#
#     # 用户名验证
#     def validate_username(self, value):
#         username = value.strip()
#         check_user = User.objects.filter(username=username)
#         if check_user:
#             raise serializers.ValidationError(u"用户名已经被注册")
#         else:
#             return username
#
#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username'],
#             is_active=False
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         # 保存用户的激活邮件内容
#         encrypt_username = make_password(
# user.username, None, 'pbkdf2_sha256')
#         host = MY_HOST
#         content = host + '/user/active/?username='
# + user.username + '&encrypt_username=' + encrypt_username
#         user_email = UserEmail(
#             user=user,
#             content=content
#         )
#         user_email.save()
#         return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            username=username, password=password
        )

        if user:
            pass
        else:
            msg = u'用户名或密码错误'
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True, write_only=True, min_length=6)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.filter(),
                message=u'当前用户名已注册'
            )
        ],
        required=True, min_length=6)
    email = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.filter(),
                message=u'当前邮箱已注册'
            )
        ],
        required=True
    )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email',
            'password'
        )

    def create(self, validated_data):
        p = validated_data.pop('password')

        user = User()
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        user.username = username
        user.email = email
        user.set_password(p)
        user.is_active = True
        user.save()

        # 保存用户的激活邮件内容
        encrypt_username = make_password(
            user.username, None, 'pbkdf2_sha256')
        host = MY_HOST
        content = host + '/user/active/?username=' + \
            user.username + '&encrypt_username=' + encrypt_username
        user_email = UserEmail(
            user=user,
            content=content
        )
        user_email.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            'id', 'user', 'real_name', 'photo', 'location',
            'interest', 'sex', 'birthday', 'introduce')
        read_only_fields = ('id', 'user',  'sex', )


# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = ('id', 'organization', 'start_date',
#                   'end_date', 'major', 'degree')
#         readonly = ('id', 'organization')
#
#
# class UserEducationSerializer(serializers.ModelSerializer):
#     user = UserSerializer(required=True)
#     edu = EducationSerializer(required=True)
#
#     class Meta:
#         model = UserEducation
#         fields = ('id', 'user', 'edu')
#         readonly = ('id', 'user', 'edu')
