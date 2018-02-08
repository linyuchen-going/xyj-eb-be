# -*- coding: UTF8 -*-
from django.conf.urls import url
from .views import OrdersApi, StatusApi

urlpatterns = [
    url("^$", OrdersApi.as_view()),
    url("^status$", StatusApi.as_view()),
]
