from django.contrib import admin

from .models import WorkOrder


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "address",
        "driver",
        "tow_truck",
        "dispatcher",
        "status",
        "created_at",
    )

    search_fields = (
        "address",
        "driver__first_name",
        "driver__last_name",
        "dispatcher__first_name",
        "dispatcher__last_name",
        "tow_truck__license_plate",
    )

    list_filter = (
        "status",
        "created_at",
    )

    ordering = ("-created_at",)

    list_select_related = (
        "driver",
        "tow_truck",
        "dispatcher",
    )

    readonly_fields = ("created_at",)
