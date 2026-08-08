from django.contrib import admin
from .models import Vehicle




# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "license_plate",
        "brand",
        "model",
        "color",
        "was_in_accident",
    )

    search_fields = (
        "license_plate",
        "brand",
        "model",
    )

    list_filter = (
        "was_in_accident",
    )
