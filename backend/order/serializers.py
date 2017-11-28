# -*- coding: UTF8 -*-
from rest_framework import serializers
from order.serializers import ProductOrderSerializer


class BackendProductOrderSerializer(serializers.ModelSerializer):
    order = ProductOrderSerializer()