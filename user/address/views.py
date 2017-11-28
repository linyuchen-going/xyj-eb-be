# -*- coding: UTF8 -*-
from rest_framework.response import Response
from rest_api.rest_api_views import LycApiBaseView
from .serializers import AddressSerializer
from .models import Address
from ..models import User


class AddressApi(LycApiBaseView):
    model_class = Address
    serializer_class = AddressSerializer
    http_method_names = ["post", "get"]


class AddressDefaultApi(LycApiBaseView):
    model_class = Address
    serializer_class = AddressSerializer
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs) -> Response:
        user: User = request.user
        return Response(self.serializer_class(user.address).data)
