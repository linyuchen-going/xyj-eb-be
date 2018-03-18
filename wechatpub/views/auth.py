# -*- coding:UTF-8 -*-
from _wechatpub.django.views.wechat_auth import WechatAuthBaseView, WechatHtmlAuthBaseView, ApiWechatAuthBase
from user.models import User


class WechatAuthView(WechatAuthBaseView):
    
    def user_info_handle(self, user_info):
        err_result = super(WechatAuthView, self).user_info_handle(user_info)
        if err_result:
            return err_result

        openid = user_info.get("openid")
        nick = user_info.get("nickname")
        user = User.objects.filter(wxopenid=openid).first()
        if not user:
            user = User(wxopenid=openid)
        user.nick = nick
        user.save()


class ApiWechatAuth(WechatAuthView, ApiWechatAuthBase):
    pass


class WechatHtmlAuthView(WechatAuthView, WechatHtmlAuthBaseView):
    pass

