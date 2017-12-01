# -*- coding: UTF8 -*-
from django.conf.urls import url, include
from .order.urls import urlpatterns as order_urls

urlpatterns = [
    url("^order/", include(order_urls))
]
