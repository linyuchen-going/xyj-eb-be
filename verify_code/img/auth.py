# -*- coding: UTF8 -*-

from verify_code.session import auth
from .config import IMG_CODE_SESSION_KEY


def verify_img_code(request, code):
    return auth.verify_code(request, IMG_CODE_SESSION_KEY, code)
