# -*- coding: UTF8 -*-
from django.conf.urls import include, url
from .address.urls import urlpatterns as address_urls
from invite_code.urls import urlpatterns as invite_code_urls
from .views import LoginWithSmsView

urlpatterns = [
    url("^address/", include(address_urls)),
    url("^invite-code/", include(invite_code_urls)),
    url("^login/sms$", LoginWithSmsView),
]
