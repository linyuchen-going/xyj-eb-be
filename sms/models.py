# -*- coding: UTF8 -*-
from django.db import models


CODE_LENGTH = 4


class SmsCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=CODE_LENGTH)
    mobile = models.CharField(max_length=11)
    used = models.BooleanField(default=False)
