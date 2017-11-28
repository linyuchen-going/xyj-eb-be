# -*- coding:UTF-8 -*-
import typing
from .models import User
from django.http.request import HttpRequest

__author__ = "linyuchen"
__doc__ = "身份验证相关"


# 后台登陆验证
class UserBackend(object):

    @staticmethod
    def authenticate(request: HttpRequest, mobile: str, password: str) -> User:
        user = User.objects.filter(mobile=mobile).first()
        if user.check_password(password):
            return user



