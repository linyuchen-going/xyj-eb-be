# -*- coding: UTF8 -*-
from uuid import uuid4

from .config import MOBILE_CODE_LENGTH, MOBILE_CODE_SESSION_KEY


def create_code(request):
    """
    生成随机验证码
    :return:
    """

    code = uuid4().hex[:MOBILE_CODE_LENGTH]
    request.session[MOBILE_CODE_SESSION_KEY] = code
    return code



