# -*- coding: UTF8 -*-
from uuid import uuid4
from .models import CODE_LENGTH, SmsCode


def create_code():
    """
    生成随机验证码
    :return:
    """
    return uuid4().hex[:CODE_LENGTH]


def verify_code(mobile, code) -> bool:

    record = SmsCode.objects.filter(used=False, mobile=mobile, code=code).first()
    if record:
        record.used = True
        record.save()
        return True

    return False
