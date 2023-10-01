from django.contrib import admin
from . import models


class OrdersAdmin(admin.ModelAdmin):
    list_display = ["pk", "order_description"]
    list_editable = ["order_description"]


# Register your models here.


admin.site.register(models.Orders, OrdersAdmin)
