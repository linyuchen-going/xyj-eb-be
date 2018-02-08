from django.contrib import admin
from .models import ProductOrder
from .models import PayOrder

admin.site.register(ProductOrder)
admin.site.register(PayOrder)
