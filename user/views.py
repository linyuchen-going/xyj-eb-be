from django.contrib.auth import login
from rest_framework.request import Request
from rest_framework.response import Response
from sms.utils import verify_code
from user.models import User
from rest_api.rest_api_views import LycApiBaseView


class LoginWithSmsView(LycApiBaseView):

    http_method_names = ["post"]
    auth_http_method_names = []

    def get(self, request: Request, *args, **kwargs):
        mobile = request.data.get("mobile")
        code = request.data.get("code")
        if verify_code(mobile, code):
            user = User.objects.get_or_create(mobile=mobile)[0]
            login(request, user)
            return Response("ok")

        return self.err_response("验证码错误")
