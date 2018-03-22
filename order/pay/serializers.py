# -*- coding: UTF8 -*-

from rest_framework import serializers
from rest_api.rest_api_field import NativeDateTimeField


# class PayOrderSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     create_time = NativeDateTimeField()
#     paid = serializers.BooleanField()
#
#     class Meta:
#         model = PayOrder
#         fields = ["id", "create_time", "paid"]
