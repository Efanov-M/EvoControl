from django.contrib import admin

# Register your models here.
from .models import TowTruck



@admin.register(TowTruck)
class TowTruckAdmin(admin.ModelAdmin):
    list_display = (
        "license_plate",
        "brand",
        "model",
        "truck_type",
        "is_active",
        "vin",
    )

    list_filter = (
        "truck_type",
        "is_active",
    )

    search_fields = (
        "license_plate",
        "brand",
        "model",
        "vin",
    )

    ordering = ("license_plate",)
