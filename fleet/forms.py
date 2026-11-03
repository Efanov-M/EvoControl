from django.forms import ModelForm, TextInput

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
