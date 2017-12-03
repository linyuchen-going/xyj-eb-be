# -*- coding: UTF8 -*-
from rest_framework.response import Response

from rest_api.rest_api_views import ApiBaseView
from verify_code.img.auth import verify_img_code
from .utils import create_code


class SmsApi(ApiBaseView):
    http_method_names = ["post"]
    auth_http_method_names = []

    def post(self, request, *args, **kwargs):

        img_code = request.data.get("imgcode")
        if not verify_img_code(request, img_code):
            return self.err_response("图片验证码有误")
        create_code(request)
        return Response("ok")
