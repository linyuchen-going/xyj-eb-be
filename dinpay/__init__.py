# -*- coding:UTF-8 -*-

from _dinpay import DinPay, AliPayParams, WechatPayParams
from server_config import DINPAY_NOTIFY_URL


DINPAY_MERCHANT_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALurkLLt6H620Kxe
xRaliqvmhw1Bj/BcHmI/SQE6wMGVMtnn+Go8DhSr7WBLcIF0vxiT502PiB3fFIxT
w8DzQvwxkaQTy+9TcpJLD4v3M7eGZSAjTKOp3Ik6oVTfWxkNVDo8Q4ALmnDIP12B
d4S4JP/+rzKRENTTcZHCEHpNDqPZAgMBAAECgYEAt9dxgFaeksLz2GdeGrlABvVl
Bw9audMD0Kq+EX5EpV5K2jvrleYOxSFHADXmmGqNaL46sDgS13BY6L6F3NZwnn9Z
XdIHV7Sfw0FePV64eCkDtwsmTJmsicJteBS3Iy+PQWulqbLkoMpu315z6qDU+36W
mTTRnMS9DJF4/pWlqCECQQDdkMFpzcHwRrV7pjfG8eg8klv6ZUrAXvv/pTtnwJTP
K9kyu959CsFm398qMa252mjZyfwt5LnbQCEZQMrFhvjbAkEA2NY++FHH9eILsvt4
HtDzbO4axg4jm1SDoe4d/QOIZSFTPqXBbE6YAE09RmJrDj46TMtXlP1E9PbFK1M+
CJTqWwJBAKFcWA/nItQLmwZXUo3YBat/Z+8fL+aUBnDzdCUmkvmiVIdnXSyx1ZJH
fq6rCXuuPehG+xqtVlIADVrn3gUnPDsCQCuN/WALrUqqeQcek+Y8umiq+x3FQUm2
FCq2lbd4ujD2HK58xPloYAfPe/tjUXWu8i7yuUjoBq3d04T8V32Jy/kCQB349KUF
ILXFvyBHL1hj2o+NTV3kGYL8fFDv5PsWgA4/KUM/OvJHjwdZ5ySwI4xz3fPFIGny
LnPr8gVT9g3PD10=
-----END PRIVATE KEY-----"""

__dinpay = DinPay("1118018253", DINPAY_MERCHANT_PRIVATE_KEY)


def create_alipay(money, product_name):
    params = AliPayParams(money, product_name, DINPAY_NOTIFY_URL, "")
    return __dinpay.create_order(params)


def create_wechatpay(money, product_name, wechat_open_id):
    params = WechatPayParams(money, product_name, DINPAY_NOTIFY_URL, "", wechat_open_id)
    return __dinpay.create_order(params)
