# -*- coding: UTF8 -*-
from django.db.models import Model
from typing import List
from order.models import ProductOrderStatus

models: List[Model] = [ProductOrderStatus]


def initdb():
    for model in models:
        if hasattr(model, "init") and callable(model.init):
            model.init()


initdb()
