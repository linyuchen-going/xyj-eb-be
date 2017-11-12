# -*- coding:UTF-8 -*-
from rest_framework.request import Request
from rest_framework.response import Response
from rest_api.rest_api_views import LycApiBaseView
from ..models import ShoppingOrder, ShoppingOrderStatus, ShareRecord, JoinShareRecord
from product.models import Product

__author__ = u"linyuchen"
__doc__ = u""


class AddOrderApi(LycApiBaseView):
    http_method_names = ["POST"]
    auth_http_method_names = ["POST"]

    # 生成订单
    def post(self, request: Request, *args, **kwargs) -> Response:
        # 参团的记录id
        join_share_record_id: int = request.data.get("join_share_record_id", 0)

        product_id: int = request.data.get("product_id", 0)
        num: int = request.data.get("product_num", 1)
        product: Product = Product.objects.filter(id=product_id).first()
        if not product:
            return self.err_response("商品id有误")
        try:
            num = int(num)
        except Exception:
            return self.err_response("商品数量有误")

        join_share_record: JoinShareRecord = JoinShareRecord.objects.filter(id=join_share_record_id).first()
        order = ShoppingOrder()
        order.set_product(product)
        order.first_payment = 0
        order.end_payment = 0
        order.num = num
        order.status = ShoppingOrderStatus.objects.get(name=ShoppingOrderStatus.STATUS_WAITE_FIRST_PAY)
        order.save()
        if join_share_record:
            join_share_record.shopping_order = order
            join_share_record.save()
        return Response()


class ShareOrderApi(LycApiBaseView):
    http_method_names = ["POST"]
    auth_http_method_names = ["POST"]

    def post(self, request: Request, *args, **kwargs) -> Response:
        order_id: int = request.data.get("order_id", 0)
        order: ShoppingOrder = ShoppingOrder.objects.filter(id=order_id).first()
        if not order:
            return self.err_response("订单id有误")

        share_record = ShareRecord()
        order.share_record = share_record
        order.save()
        return Response()


class JoinShareOrderApi(LycApiBaseView):
    http_method_names = ["POST"]
    auth_http_method_names = ["POST"]

    def post(self, request: Request, *args, **kwargs) -> Response:
        share_record_id = request.data.get("share_id", 0)
        share_record: ShareRecord = ShareRecord.objects.filter(id=share_record_id).first()
        join_record = share_record.join_records.filter(user=request.user).first()
        if not join_record:
            # return self.err_response("已经参与此团购")
            join_record = JoinShareRecord(user=request.user)
            join_record.save()
            share_record.join_records.add(join_record)

        return Response({"join_share_record_id": join_record.id})

