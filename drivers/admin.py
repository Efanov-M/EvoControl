from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Drivers




# Register your models here.
@admin.register(Drivers)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "license_driver",
        
    )

    search_fields = (
        "first_name",
        "license_driver",
    )

    list_filter = (
        "license_driver",
        "first_name",
    )
