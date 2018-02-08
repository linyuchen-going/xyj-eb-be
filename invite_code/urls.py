# -*- coding: UTF8 -*-
from django.conf.urls import url
from .views import InviteCodesApi

urlpatterns = [
    url("^$", InviteCodesApi.as_view())
]
