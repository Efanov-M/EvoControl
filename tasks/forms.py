from django.forms import ModelForm

from tasks.models import WorkOrder


class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrder
        fields = ["address", "driver", "tow_truck", "dispatcher", "comment"]
