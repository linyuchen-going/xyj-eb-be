# -*- coding: UTF8 -*-
from rest_api.rest_api_views import LycApiBaseView
from .serializers import InviteCodeSerializer, InviteCode
from user.models import User


class InviteCodesApi(LycApiBaseView):
    model_class = InviteCode
    serializer_class = InviteCodeSerializer
    http_method_names = ["get"]
    auth_http_method_names = ["get"]

    def get_queryset(self):
        user: User = self.request.user
        return user.invite_codes.all()
