from django.forms import ModelChoiceField, ModelForm

from drivers.models import Drivers
from fleet.models import TowTruck
from operations.models import EvacuationCase


class EvacuationCaseForm(ModelForm):
    driver = ModelChoiceField(
        queryset=Drivers.objects.all(),
        label="Водитель",
        required=True,
    )
    tow_truck = ModelChoiceField(
        queryset=TowTruck.objects.all(), label="Эвакуаторы", required=True
    )

    class Meta:
        model = EvacuationCase
        fields = ["vehicle"]
