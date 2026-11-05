from django.contrib import admin

from .models import WorkOrder


# Register your models here.
@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ("address", "driver", "tow_truck", "dispatcher", "status", "comment")

    search_fields = (
        "address",
        "driver",
        "dispatcher",
        "status",
    )
