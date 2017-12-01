from rest_framework.response import Response
from rest_api.rest_api_views import LycApiBaseView
from .serializers import ProductOrderSerializer, NewProductOrderSerializer
from .models import ProductOrder, ProductOrderStatus
from user.models import Address, User
from invite_code.models import InviteCode


class ProductOrdersApi(LycApiBaseView):
    model_class = ProductOrder
    serializer_class = ProductOrderSerializer
    http_method_names = ["get"]
    auth_http_method_names = ["get"]

    def get_queryset(self):
        user = self.request.user
        queryset = self.model_class.objects.filter(user=user)
        return queryset


class ProductOrderDetailApi(LycApiBaseView):
    model_class = ProductOrder
    serializer_class = ProductOrderSerializer
    http_method_names = ["get"]
    auth_http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        user: User = self.request.user
        order = self.model_class.objects.filter(user=user, id=kwargs.get("id")).first()
        if not order:
            return self.err_response("订单id有误")
        return Response(self.serializer_class(order).data)


class NewProductOrderApi(LycApiBaseView):

    model_class = ProductOrder
    serializer_class = NewProductOrderSerializer
    http_method_names = ["post"]
    auth_http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        request.data["status"] = ProductOrderStatus.objects.get(name=ProductOrderStatus.STATUS_WAIT_PAY).id

        # 检查invite_code
        invite_code = request.data.get("invite_code")
        invite_code: InviteCode = InviteCode.objects.filter(code=invite_code).first()
        if not invite_code:
            return self.err_response("邀请码有误")
        if invite_code.is_used():
            return self.err_response("邀请码已失效")

        # 收货地址复制一份出来保存
        address = Address.objects.filter(id=request.data.get("address")).first()
        if not address:
            return self.err_response("收货地址id有误")
        address.id = None
        address.save()
        request.data["address"] = address.id
        request.user.default_address = address
        request.user.save()

        # 订单关联用户
        request.data["user"] = request.user.id

        response = super(NewProductOrderApi, self).post(request, *args, **kwargs)

        # 创建订单失败时删除地址副本
        if not response.data.get("id"):
            address.delete()

        return response

