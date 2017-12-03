# -*- coding: UTF8 -*-
from django.conf.urls import url
from .views import SmsApi

urlpatterns = [
    url("^$", SmsApi.as_view())
]