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
    pay_order = models.ForeignKey(PayOrder, null=True, blank=True)
    product = models.ForeignKey("product.Product")
    num = models.IntegerField(default=1)
    invite_code = models.CharField(max_length=CODE_LENGTH, null=False)
    user = models.ForeignKey("user.User")
    status = models.ForeignKey(ProductOrderStatus)
    address = models.ForeignKey("user.Address")
    sf_no = models.CharField(max_length=30, null=True, blank=True)  # 顺丰单号

