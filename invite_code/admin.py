# -*- coding: UTF8 -*-
from django.contrib import admin
from .models import InviteCode, InviteCodeConfig

admin.site.register(InviteCode)
admin.site.register(InviteCodeConfig)
