# -*- coding: UTF8 -*-
from django.conf.urls import url
from .views import ImgCodeApi

urlpatterns = [
    url("^$", ImgCodeApi.as_view())
]
