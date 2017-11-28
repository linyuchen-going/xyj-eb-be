# -*- coding: UTF8 -*-

from rest_framework import serializers
from rest_api.rest_api_field import NativeDateTimeField
from .models import ProductOrder, ProductOrderStatus
from product.serializers import ProductSerializer
from .pay.serializers import PayOrderSerializer


class ProductOrderStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOrderStatus
        fields = ["id", "name"]


class ProductOrderSerializer(serializers.ModelSerializer):
    create_time = NativeDateTimeField()
    product = ProductSerializer()
    pay_order = PayOrderSerializer()
    status = ProductOrderStatusSerializer()

    class Meta:
        model = ProductOrder
        fields = ["id", "create_time", "product", "pay_order", "status"]
