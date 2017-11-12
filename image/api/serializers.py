# -*- coding:UTF-8 -*-
from rest_framework import serializers
from rest_api.rest_api_field import CustomBaseField
from ..models import Image

__author__ = u"linyuchen"
__doc__ = u""


class ImageField(CustomBaseField):
    def to_representation(self, value: Image):
        return value.url
