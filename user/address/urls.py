# -*- coding: UTF8 -*-

from django.conf.urls import url
from .views import AddressApi, AddressDefaultApi

urlpatterns = [
    url(r"^$", AddressApi.as_view()),
    url(r"^default$", AddressDefaultApi.as_view())
]
