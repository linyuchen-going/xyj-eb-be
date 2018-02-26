from .pay.models import *
# from .shopping.models import *
from django.db import models
from django.utils import timezone
from invite_code.models import CODE_LENGTH


class ProductOrderStatus(models.Model):
    STATUS_WAIT_PAY = "待付款"
    STATUS_PAID = "日本下单"
    STATUS_WAIT_CHINA = "日本到货待入关"
    STATUS_SEND = "已发货"

    name = models.CharField(max_length=20)

    @staticmethod
    def init():
        ProductOrderStatus.objects.get_or_create(name=ProductOrderStatus.STATUS_WAIT_PAY)
        ProductOrderStatus.objects.get_or_create(name=ProductOrderStatus.STATUS_PAID)
        ProductOrderStatus.objects.get_or_create(name=ProductOrderStatus.STATUS_WAIT_CHINA)
        ProductOrderStatus.objects.get_or_create(name=ProductOrderStatus.STATUS_SEND)


class ProductOrder(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    pay_order = models.ForeignKey(PayOrder, null=True, blank=True, on_delete=None)
    product = models.ForeignKey("product.Product", on_delete=None)
    num = models.IntegerField(default=1)
    invite_code = models.CharField(max_length=CODE_LENGTH, null=True)
    user = models.ForeignKey("user.User", on_delete=None)
    status = models.ForeignKey(ProductOrderStatus, on_delete=None)
    address = models.ForeignKey("user.Address", on_delete=None)
    sf_no = models.CharField(max_length=30, null=True, blank=True)  # 顺丰单号

