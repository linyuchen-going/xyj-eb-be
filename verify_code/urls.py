# -*- coding: UTF8 -*-
from django.conf.urls import url, include
from .sms.urls import urlpatterns as sms_urls
from .img.urls import urlpatterns as img_urls

urlpatterns = [
    url("sms/", include(sms_urls)),
    url("img/", include(img_urls))
]