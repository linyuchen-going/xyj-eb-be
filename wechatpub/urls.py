# -*- coding:UTF-8 -*-

from django.conf.urls import url
from .views.auth import WechatHtmlAuthView
from .pay.views import WechatPayResultView
from _wechatpub.django.views.message import WechatPubMessageBaseView

urlpatterns = [
    url(r"^fe/(?P<html_name>.+\.html$)", WechatHtmlAuthView.as_view()),
    url(r"^pay/result$", WechatPayResultView.as_view()),
    url(r"^message$", WechatPubMessageBaseView.as_view())
]
