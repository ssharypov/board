from django.contrib import admin
from . import models


class OrdersAdmin(admin.ModelAdmin):
    list_display = ["pk", "date", "order_description", "approved"]
    list_editable = ["order_description", "approved"]

class CustomersAdmin(admin.ModelAdmin):
    list_display = ["pk", "nickname", "tlg_id", "tlg_contact"]

# Register your models here.


admin.site.register(models.Orders, OrdersAdmin)
admin.site.register(models.Customers, CustomersAdmin)
