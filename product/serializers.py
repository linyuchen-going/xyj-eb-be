# -*- coding:UTF-8 -*-
from rest_framework import serializers
from image.api.serializers import ImageField
from product.models import Product

__author__ = u"linyuchen"
__doc__ = u""


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    cover = ImageField()
    images = serializers.ListField(source="images.all", child=ImageField())

    class Meta:
        model = Product
        fields = ["id", "name", "price", "cover", "images", "describe"]
