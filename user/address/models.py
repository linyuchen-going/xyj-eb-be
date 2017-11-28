# -*- coding: UTF8 -*-
from django.db import models


class Address(models.Model):

    country = models.CharField(max_length=10)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    area = models.CharField(max_length=10, null=True, blank=True)
    detail = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=11)
    name = models.CharField(max_length=20)
