# -*- coding:UTF-8 -*-

__author__ = "linyuchen"
__doc__ = """
"""
import os
import uuid
from django.conf import settings
from _wechatpub.pay import WechatPayApiBase
from rest_api.tools.mail import send_mail_to_admin
from .models import WechatPayOrder


class WechatPay(WechatPayApiBase):
    def __init__(self):
        cert_path = os.path.join(os.path.dirname(__file__), "certs")

        super(WechatPay, self).__init__(os.path.join(cert_path, "apiclient_cert.pem"),
                                        os.path.join(cert_path, "apiclient_key.pem"), mch_id=settings.WECHAT_PAY_MCHID,
                                        pay_key=settings.WECHAT_PAY_KEY, wechatpub_appid=settings.WECHAT_PUB_APPID)

    def api_err_handle(self, err_code, err_msg):
        send_mail_to_admin("微信支付api出错", f"{err_code}: {err_msg}")

    def create_order(self, order_summary, out_trade_no, money, product_id, to_user, response_data: dict):
        money = money * 100

        def jssdk_callback(data):
            response_data["wechat_pay_data"] = data
        success, err_code, err_msg = super(WechatPay, self).create_order(order_summary=order_summary,
                                                                         out_trade_no=out_trade_no,
                                                                         money=money, trade_type="JSAPI",
                                                                         product_id=product_id, to_user=to_user,
                                                                         notify_url=settings.HTTP_HOST + "/wechatpub/pay/result",
                                                                         jssdk_sign_callback=jssdk_callback)
        return success, err_code, err_msg
