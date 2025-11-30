from django.contrib import admin
from . import models
from .models import Outflow


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('product__title',)


admin.site.register(models.Outflow, OutflowAdmin)

class OutflowAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "value", "costumer", "created_at")
    list_filter = ("costumer",)
    search_fields = ("product__name", "costumer__name")
