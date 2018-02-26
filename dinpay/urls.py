# -*- coding:UTF-8 -*-

from django.conf.urls import url
from .views import PayResult

urlpatterns = [
    url("^notify$", PayResult.as_view())
]
