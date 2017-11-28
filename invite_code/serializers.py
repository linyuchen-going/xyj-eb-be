# -*- coding: UTF8 -*-
from rest_framework import serializers
from .models import InviteCode


class InviteCodeSerializer(serializers.ModelSerializer):
    used = serializers.BooleanField(source="is_used")
    rest_time = serializers.CharField(source="rest_available_time")

    class Meta:
        model = InviteCode
        fields = ["id", "used", "rest_time", "code"]
