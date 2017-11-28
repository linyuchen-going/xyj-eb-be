# -*- coding: UTF8 -*-

from rest_framework import serializers
from rest_api.rest_api_field import NativeDateTimeField
from .models import PayOrder


class PayOrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    create_time = NativeDateTimeField()
    paid = serializers.BooleanField()

    class Meta:
        model = PayOrder
        fields = ["id", "create_time", "paid"]
