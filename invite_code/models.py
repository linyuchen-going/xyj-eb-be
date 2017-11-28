# -*- coding: UTF8 -*-

from django.db import models
from django.utils import timezone


CODE_LENGTH = 8


class InviteCodeConfig(models.Model):
    available_seconds = models.IntegerField(default=7 * 24 * 3600)  # 邀请码的有效期

    @staticmethod
    def get_config():
        config = InviteCodeConfig.objects.first()
        if not config:
            config = InviteCodeConfig()
            config.save()
        return config


class InviteCode(models.Model):
    code = models.CharField(max_length=CODE_LENGTH, unique=True)
    create_time = models.DateTimeField(default=timezone.now)
    used_time = models.DateTimeField(null=True, blank=True)

    def is_used(self):
        return bool(self.used_time)

    def rest_available_time(self)-> str:
        used_seconds = (timezone.now() - self.create_time).total_seconds()
        seconds = InviteCodeConfig.get_config().available_seconds - used_seconds
        seconds = int(seconds)
        minute = int(seconds / 60)
        hour = int(minute / 60)
        day = int(hour / 24)

        seconds = seconds % 60  # 除去分钟数后的剩余秒数
        minute = minute % 60  # 除去小时数后的剩余秒数
        hour = hour % 24  # 除去天数后的剩余小时数

        # t = f"{hour}小时{minute}分{seconds}秒"
        t = f"{hour}小时{minute}分"
        if day:
            t = f"{day}天" + t
        return t

    def __str__(self):
        return self.code