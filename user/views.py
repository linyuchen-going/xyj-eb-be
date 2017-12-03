from django.contrib.auth import login
from rest_framework.request import Request
from rest_framework.response import Response

from rest_api.rest_api_views import ApiBaseView
from user.models import User
from verify_code.sms.auth import verify_sms_code


class LoginWithSmsView(ApiBaseView):

    http_method_names = ["post"]
    auth_http_method_names = []

    def post(self, request: Request, *args, **kwargs):
        mobile = request.data.get("mobile")
        code = request.data.get("code")
        if verify_code(request, code):
            user = User.objects.get_or_create(mobile=mobile)[0]
            login(request, user)
            return Response("ok")

        return self.err_response("手机验证码错误")
