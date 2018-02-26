# -*- coding:UTF-8 -*-

from _dinpay import DinPay, AliPayParams, WechatPayParams, DinPayWay
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
# DINPAY_MERCHANT_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
# MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALf/+xHa1fDTCsLY
# PJLHy80aWq3djuV1T34sEsjp7UpLmV9zmOVMYXsoFNKQIcEzei4QdaqnVknzmIl7
# n1oXmAgHaSUF3qHjCttscDZcTWyrbXKSNr8arHv8hGJrfNB/Ea/+oSTIY7H5cAtW
# g6VmoPCHvqjafW8/UP60PdqYewrtAgMBAAECgYEAofXhsyK0RKoPg9jA4NabLuuu
# u/IU8ScklMQIuO8oHsiStXFUOSnVeImcYofaHmzIdDmqyU9IZgnUz9eQOcYg3Bot
# UdUPcGgoqAqDVtmftqjmldP6F6urFpXBazqBrrfJVIgLyNw4PGK6/EmdQxBEtqqg
# XppRv/ZVZzZPkwObEuECQQDenAam9eAuJYveHtAthkusutsVG5E3gJiXhRhoAqiS
# QC9mXLTgaWV7zJyA5zYPMvh6IviX/7H+Bqp14lT9wctFAkEA05ljSYShWTCFThtJ
# xJ2d8zq6xCjBgETAdhiH85O/VrdKpwITV/6psByUKp42IdqMJwOaBgnnct8iDK/T
# AJLniQJABdo+RodyVGRCUB2pRXkhZjInbl+iKr5jxKAIKzveqLGtTViknL3IoD+Z
# 4b2yayXg6H0g4gYj7NTKCH1h1KYSrQJBALbgbcg/YbeU0NF1kibk1ns9+ebJFpvG
# T9SBVRZ2TjsjBNkcWR2HEp8LxB6lSEGwActCOJ8Zdjh4kpQGbcWkMYkCQAXBTFiy
# yImO+sfCccVuDSsWS+9jrc5KadHGIvhfoRjIj2VuUKzJ+mXbmXuXnOYmsAefjnMC
# I6gGtaqkzl527tw=
# -----END PRIVATE KEY-----"""

__dinpay = DinPay("1118018253", DINPAY_MERCHANT_PRIVATE_KEY)
# __dinpay = DinPay("1111110166", DINPAY_MERCHANT_PRIVATE_KEY)


def create_alipay(money, product_name):
    params = AliPayParams(money, product_name, DINPAY_NOTIFY_URL, "")
    return __dinpay.create_order(params)


def create_wechatpay(money, product_name, wechat_open_id):
    params = WechatPayParams(money, product_name, DINPAY_NOTIFY_URL, "", wechat_open_id)
    return __dinpay.create_order(params)


test_data = {
    "input_charset": "UTF-8",
    "interface_version": "V3.0",
    "merchant_code": "1111110166",
    "order_no": "1",
    "order_time": "2018-02-26 00:00:00",
    "order_amount": "0.1",
    "product_name": "testpay",
    "notify_url": "http://www.kxshanghai.com/api/verify-code/sms",
    "service_type": "alipay_h5"
}
# print(__dinpay.make_sign(test_data))