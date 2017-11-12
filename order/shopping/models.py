from django.db import models
from django.utils import timezone
from django.db.models import QuerySet

__author__ = "linyuchen"
__doc__ = "购物订单"


class ShoppingOrderStatus(models.Model):
    STATUS_WAITE_FIRST_PAY = "待定金"
    STATUS_FIRST_PAID = "已付定金"
    STATUS_WAITE_END_PAY = "待付尾款"  # 到货了，需要用户付尾款然后发货
    STATUS_END_PAID = "已付尾款"
    STATUS_SEND = "已发货"
    STATUS_FINISH = "已收货"

    name = models.CharField(max_length=10, unique=True)

    def init(self):
        ShoppingOrderStatus.objects.get_or_create(name=ShoppingOrderStatus.STATUS_WAITE_FIRST_PAY)
        ShoppingOrderStatus.objects.get_or_create(name=ShoppingOrderStatus.STATUS_FIRST_PAID)
        ShoppingOrderStatus.objects.get_or_create(name=ShoppingOrderStatus.STATUS_WAITE_END_PAY)
        ShoppingOrderStatus.objects.get_or_create(name=ShoppingOrderStatus.STATUS_END_PAID)
        ShoppingOrderStatus.objects.get_or_create(name=ShoppingOrderStatus.STATUS_SEND)
        ShoppingOrderStatus.objects.get_or_create(name=ShoppingOrderStatus.STATUS_FINISH)


class ShoppingOrder(models.Model):
    product = models.ForeignKey("product.Product")
    price = models.FloatField()  # 购买时价格
    name = models.CharField(max_length=32)  # 购买时商品名字
    num = models.IntegerField()  # 购买的数量
    create_time = models.DateTimeField(default=timezone.now)
    first_payment = models.FloatField()  # 首付/定金金额
    end_payment = models.FloatField()  # 尾款金额
    status = models.ForeignKey(ShoppingOrderStatus)
    share_record = models.ForeignKey("ShareRecord", null=True, blank=True)
    pay_order = models.ForeignKey("order.PayOrder", null=True, blank=True)

    def set_product(self, product):
        self.product = product
        self.price = product.price
        self.name = product.name

    def is_paid(self) -> bool:
        return self.pay_order and self.pay_order.paid


class ShareSetting(models.Model):

    # 最少几人成团
    min_join_num = models.IntegerField(default=3)

    # 成团后的到货时间
    success_arrival_day = models.IntegerField(default=14)

    @staticmethod
    def get_setting():
        setting = ShareSetting.objects.first()
        if not setting:
            setting = ShareSetting()
            setting.save()
        return setting


class ShareRecord(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    join_records = models.ManyToManyField("JoinShareRecord", blank=True)

    def is_success(self) -> bool:
        setting = ShareSetting.get_setting()
        return self.join_paid_records().count() >= setting.min_join_num

    # 已经付款了的参团记录
    def join_paid_records(self) -> QuerySet:
        return self.join_records.filter(sharerecord__shoppingorder__pay_order__paid=True)


class JoinShareRecord(models.Model):
    user = models.ForeignKey("user.User")
    create_time = models.DateTimeField(default=timezone.now)
    shopping_order = models.ForeignKey(ShoppingOrder, null=True, blank=True)
