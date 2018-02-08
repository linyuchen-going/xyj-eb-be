# -*- coding: UTF8 -*-
from rest_framework.response import Response
from .config import MOBILE_SESSION_KEY
from rest_api.rest_api_views import ApiBaseView
from verify_code.img.auth import verify_img_code
from .utils import create_code
from .ucpass.send import send


class SmsApi(ApiBaseView):
    http_method_names = ["post"]
    auth_http_method_names = []

    def post(self, request, *args, **kwargs):

        img_code = request.data.get("imgcode")
        mobile = request.data.get("mobile", "")
        if not mobile:
            return self.err_response("手机号不能为空")
        if not mobile.isdigit() or len(mobile) != 11:
            return self.err_response("手机号不正确")

        if not verify_img_code(request, img_code):
            return self.err_response("图片验证码有误")
        sms_code = create_code(request)
        success, msg = send(mobile, sms_code)
        if success:
            request.session[MOBILE_SESSION_KEY] = mobile
            return Response("ok")
        else:
            return self.err_response(f"验证码发送失败,{msg}")
