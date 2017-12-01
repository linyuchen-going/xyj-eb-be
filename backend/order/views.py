# -*- coding: UTF8 -*-
from rest_framework.permissions import IsAdminUser
from rest_api.rest_api_views import PagesApi, LycApiBaseView
from order.serializers import ProductOrderSerializer, ProductOrderStatusSerializer
from order.models import ProductOrder, ProductOrderStatus
from .serializers import ChangeOrderStatusSerializer


class OrdersApi(PagesApi):
    model_class = ProductOrder
    serializer_class = ProductOrderSerializer
    permission_classes = [IsAdminUser]
    auth_http_method_names = ["get"]
    http_method_names = ["get"]
    # num_of_page = 4

    def get_queryset(self):
        queryset = self.model_class.objects.all().order_by("-create_time")
        return self.pages_queryset(queryset)


class StatusApi(LycApiBaseView):
    permission_classes = [IsAdminUser]
    auth_http_method_names = ["get", "post"]
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        self.model_class = ProductOrderStatus
        self.serializer_class = ProductOrderStatusSerializer
        return super(StatusApi, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.model_class = ProductOrder
        self.serializer_class = ChangeOrderStatusSerializer
        return super(StatusApi, self).post(request, *args, **kwargs)
