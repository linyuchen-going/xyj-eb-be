# -*- coding: UTF8 -*-
from verify_code.session import auth
from .config import MOBILE_CODE_SESSION_KEY


def verify_sms_code(request, code):
    return auth.verify_code(request, MOBILE_CODE_SESSION_KEY, code)
