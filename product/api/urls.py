# -*- coding:UTF-8 -*-
from django.conf.urls import url
from .views import ProductApi
__author__ = u"linyuchen"
__doc__ = u""


urlpatterns = [
    url(r"(?P<id>\d+)", ProductApi.as_view())
]
