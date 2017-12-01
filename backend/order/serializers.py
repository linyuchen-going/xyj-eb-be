# -*- coding: UTF8 -*-
from rest_framework import serializers
from order.models import ProductOrder, ProductOrderStatus


class ChangeOrderStatusSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    status = serializers.PrimaryKeyRelatedField(queryset=ProductOrderStatus.objects.all())

    class Meta:
        model = ProductOrder
        fields = ("id", "status")


class OrderStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOrderStatus
        fields = ("id", "name")
