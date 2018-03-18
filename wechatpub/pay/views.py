# -*- coding:UTF-8 -*-
from django.views.generic import View
from django.http.response import HttpResponse

__author__ = "linyuchen"
__doc__ = """
"""


class WechatPayResultView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse("")
