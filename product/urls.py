# -*- coding:UTF-8 -*-
from django.conf.urls import url
from .views import ProductApi, AllProductsApi
__author__ = u"linyuchen"
__doc__ = u""


urlpatterns = [
    url(r"(?P<id>\d+)", ProductApi.as_view()),
    url(r"^all$", AllProductsApi.as_view())
]
