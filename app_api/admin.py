from django.contrib import admin
from . import models

class CheckCodes(admin.ModelAdmin):
    list_display = ["pk", "code_string", "generation_time"]
# Register your models here.

admin.site.register(models.Code, CheckCodes)