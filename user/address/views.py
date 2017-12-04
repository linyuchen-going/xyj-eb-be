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
    auth_http_method_names = ["get", "post"]

    def get_queryset(self):
        return self.request.user.address.all()

    def post(self, request, *args, **kwargs):
        response = super(AddressApi, self).post(request, *args, **kwargs)
        address_id = response.data.get("id")
        if address_id:
            address = self.model_class.objects.filter(id=address_id).first()
            if address not in self.request.user.address.all():
                self.request.user.address.add(address)
        return response

    def check_model_save_permission(self, queryset_item):
        return queryset_item in self.request.user.address.all()


class AddressDefaultApi(LycApiBaseView):
    model_class = Address
    serializer_class = AddressSerializer
    http_method_names = ["get"]
    auth_http_method_names = ["get"]

    def get(self, request, *args, **kwargs) -> Response:
        user: User = request.user
        return Response(self.serializer_class(user.default_address).data)
