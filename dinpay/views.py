# -*- coding:UTF-8 -*-
from django.views.generic import View
from django.http.response import HttpResponse


class PayResult(View):

    def post(self, request, *args, **kwargs):
        HttpResponse("ok")
