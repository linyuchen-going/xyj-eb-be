# -*- coding:UTF-8 -*-

__author__ = "linyuchen"
__doc__ = """
"""
from django.db import models
from django.utils import timezone


class WechatPayOrder(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    out_id = models.TextField()
    money = models.FloatField()  # 单位元
    paid = models.BooleanField(default=False)
