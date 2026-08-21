from vehicles.models import Vehicle
from django.forms import ModelForm



class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
