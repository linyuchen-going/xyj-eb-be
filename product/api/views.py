# -*- coding:UTF-8 -*-
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_api.rest_api_views import LycApiBaseView
from ..models import Product
from .serializers import ProductSerializer

__author__ = u"linyuchen"
__doc__ = u""


class ProductApi(LycApiBaseView):
    model_class = Product
    serializer_class = ProductSerializer
    http_method_names = ['get']
    permission_classes = []
    auth_http_method_names = []

    def get(self, request, *args, **kwargs) -> Response:
        return Response(self.serializer_class(self.model_class.objects.filter(id=kwargs.get("id")).first()).data)
