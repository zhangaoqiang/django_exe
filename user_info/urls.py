# -*- coding: utf-8 -*-
from django.conf.urls import url
from user_info import views

urlpatterns = [

    url(r'^signin/', views.SignIn.as_view()),
    url(r'^signup/', views.SignUp.as_view()),
    url(r'^active/', views.ActiveAccount.as_view()),

]
