# Register your models here.
from django.contrib import admin

from .models import Dispatchers


# Register your models here.
@admin.register(Dispatchers)
class DispatcherAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "place_work",
        "employee_number",
    )

    search_fields = (
        "first_name",
        "last_name",
        "place_work",
        "employee_number",
    )
