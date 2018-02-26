# -*- coding:UTF-8 -*-
import uuid
import base64
from typing import TypeVar
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
from datetime import datetime


class DinPayWay:
    WECHAT = "wxpub_pay"
    ALIPAY = "alipay_h5"


class PayParams(object):
    amount: float = 0.0  # 订单金额，单位元，精确到两位小数
    product_name: str = ""
    notify_url: str = ""  # 支付结果通知url，支付完成后会post一些数据到此url
    return_url: str = ""  # 支付完成后跳转的页面url
    sign_type: str = "RSA-S"
    service_type = ""

    def __init__(self, amount: float, product_name: str, notify_url: str, return_url: str):
        self.amount = amount
        self.product_name = product_name
        self.notify_url = notify_url
        self.return_url = return_url

    def to_dict(self):
        return {
            "order_amount": self.amount,
            "product_name": self.product_name,
            "notify_url": self.notify_url,
            "return_url": self.return_url,
            "sign_type": self.sign_type,
            "service_type": self.service_type
        }


class WechatPayParams(PayParams):
    open_id: str = ""
    service_type = DinPayWay.WECHAT

    def __init__(self, amount: float, product_name: str, notify_url: str, return_url: str, open_id: str):
        super(WechatPayParams, self).__init__(amount, product_name, notify_url, return_url)
        self.open_id = open_id

    def to_dict(self):
        data = super(WechatPayParams, self).to_dict()
        data["open_id"] = self.open_id
        return data


class AliPayParams(PayParams):
    service_type = DinPayWay.ALIPAY


OrderPayParams = TypeVar("OrderPayParams", WechatPayParams, AliPayParams)


class DinPay(object):

    def __init__(self, merchant_code: str, merchant_private_key: str):
        """
        :param merchant_code: 商户号
        """
        self.token = ""
        self.merchant_code = merchant_code
        # self.merchant_private_key = rsa.PrivateKey.load_pkcs1(merchant_private_key)
        self.merchant_private_key = RSA.importKey(merchant_private_key)
        self.pay_url = "https://pay.dinpay.com/gateway?input_charset=UTF-8"

    def __create_order(self, params: PayParams):
        """
        :return:
        """

        pdata = {
            "merchant_code": self.merchant_code,
            "order_no": uuid.uuid4().hex,
            "interface_version": "V3.0",
            "input_charset": "UTF-8",
            "order_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        pdata.update(params.to_dict())
        new_data = {}
        for k in pdata:
            if pdata[k]:
                new_data[k] = pdata[k]
        return new_data

    def create_order(self, params: OrderPayParams):
        """

        :param params:
        :return: dict, post的各项参数
        """
        pdata = self.__create_order(params)
        sign = self.make_sign(pdata)
        pdata["sign"] = sign
        return pdata

    def make_sign(self, pdata: dict):
        sign_str_list = []
        for k in sorted(pdata.keys()):
            if k == "sign_type":
                continue
            sign_str_list.append("%s=%s" % (k, pdata[k]))
        sign_str = "&".join(sign_str_list).encode("utf8")
        signer = PKCS1_v1_5.new(self.merchant_private_key)
        m = MD5.new()
        m.update(sign_str)
        sign = signer.sign(m)
        sign = base64.b64encode(sign).decode("utf8")
        return sign
