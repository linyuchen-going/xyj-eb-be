# -*- coding: UTF8 -*-

from _wechatpub import WechatPubApiBase
from django.conf import settings

WECHATPUB_API = WechatPubApiBase(appid=settings.WECHAT_PUB_APPID, appsecret=settings.WECHAT_PUB_APPSECRET)
