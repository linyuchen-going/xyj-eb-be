# -*- coding:UTF-8 -*-
from django.db import models
from django.utils import timezone

__author__ = u"linyuchen"
__doc__ = u""


class PayOrder(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField()
