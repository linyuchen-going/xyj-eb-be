from django.contrib.auth import login, logout
from rest_framework.request import Request
from rest_framework.response import Response
from rest_api.rest_api_views import ApiBaseView
from user.models import User
from verify_code.sms.auth import verify_sms_code
from verify_code.sms.config import MOBILE_SESSION_KEY


class LoginWithSmsApi(ApiBaseView):

    http_method_names = ["post"]
    auth_http_method_names = []

    def post(self, request: Request, *args, **kwargs):
        mobile = request.session.get(MOBILE_SESSION_KEY)
        code = request.data.get("code")
        if verify_sms_code(request, code):
            user = User.objects.get_or_create(mobile=mobile)[0]
            login(request, user)
            return Response("ok")

        return self.err_response("手机验证码错误")


class LoginStatusApi(ApiBaseView):

    http_method_names = ["get"]
    auth_http_method_names = []

    def get(self, request, *args, **kwargs):
        status = request.user.is_authenticated()
        return Response({"status": status})


class LogoutApi(ApiBaseView):
    http_method_names = ["get"]
    auth_http_method_names = []

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response("ok")
