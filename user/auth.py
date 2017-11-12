# -*- coding:UTF-8 -*-
import typing
from .models import User
from django.http.request import HttpRequest

__author__ = u"linyuchen"
__doc__ = u""


# 后台登陆验证
class UserBackend(object):
    def authenticate(self, request: HttpRequest, mobile: str, password: str) -> User:
        user = User.objects.filter(mobile=mobile).first()
        if user.check_password(password):
            return user
