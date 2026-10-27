from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
from vehicles.models import Vehicle


class VehicleForm(ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'

        widgets = {
            'license_plate': TextInput(
                attrs={
                    'placeholder': 'Например, А123ВС77'
                }
            )
        }
