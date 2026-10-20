from django.forms import ModelForm
from django.core.exceptions import ValidationError
from vehicles.models import Vehicle


class VehicleForm(ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'
