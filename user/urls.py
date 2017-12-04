# -*- coding: UTF8 -*-
from django.conf.urls import include, url
from .address.urls import urlpatterns as address_urls
from invite_code.urls import urlpatterns as invite_code_urls
from .views import LoginWithSmsApi, LoginStatusApi, LogoutApi

urlpatterns = [
    url("^address/", include(address_urls)),
    url("^invite-code/", include(invite_code_urls)),
    url("^login/sms$", LoginWithSmsApi.as_view()),
    url("^login/status$", LoginStatusApi.as_view()),
    url("^logout$", LogoutApi.as_view()),
]
