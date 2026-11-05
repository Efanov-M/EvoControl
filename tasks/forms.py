from django.forms import ModelForm

from tasks.models import WorkOrder


class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            "address",
            "driver",
            "dispatcher",
            "comment",
        ]

    def clean_driver(self):
        driver = self.cleaned_data["driver"]

        driver_changed = not self.instance.pk or self.instance.driver_id != driver.pk

        if driver_changed and not driver.tow_truck_id:
            from django.core.exceptions import ValidationError

            raise ValidationError("У выбранного водителя нет закреплённого эвакуатора.")

        return driver
