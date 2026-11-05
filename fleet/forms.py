from django import forms
from django.forms import ModelForm, TextInput

from drivers.models import Drivers
from fleet.models import TowTruck


class TowTruckForm(ModelForm):
    class Meta:
        model = TowTruck
        fields = "__all__"

        widgets = {
            "license_plate": TextInput(attrs={"placeholder": "Например, А123ВС77"}),
            "vin": TextInput(attrs={"placeholder": "Например, XTA210990Y1234567"}),
        }

        help_texts = {
            "vin": (
                "VIN — уникальный идентификационный номер "
                "транспортного средства, состоящий из 17 символов "
                "(латинские буквы и цифры, кроме I, O и Q)."
            )
        }


class TowTruckAssignmentForm(TowTruckForm):
    assigned_drivers = forms.ModelMultipleChoiceField(
        queryset=Drivers.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Закреплённые водители",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields[
                "assigned_drivers"
            ].initial = self.instance.assigned_drivers.all()
