# -*- coding: UTF8 -*-
from django.conf.urls import url
from .views import ProductOrdersApi

urlpatterns = [
    url("^product$", ProductOrdersApi.as_view())
]
