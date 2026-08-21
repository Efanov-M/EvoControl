from django.contrib import admin

from operations.models import ParkingLot


@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "address",
    )

    ordering = ("name",)
