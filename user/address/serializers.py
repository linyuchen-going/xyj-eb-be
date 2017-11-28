# -*- coding: UTF8 -*-
from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)
    country = serializers.CharField(default="中国", allow_blank=True)
    province = serializers.CharField()
    city = serializers.CharField()
    area = serializers.CharField()
    detail = serializers.CharField()
    zipcode = serializers.CharField(allow_null=True, allow_blank=True)
    name = serializers.CharField()
    mobile = serializers.CharField()

    class Meta:
        model = Address
        fields = ["id", "country", "province", "city", "area", "detail", "zipcode", "name", "mobile"]
