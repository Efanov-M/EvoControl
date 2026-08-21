from fleet.models import TowTruck
from django.forms import ModelForm



class TowTruckForm(ModelForm):
    class Meta:
        model = TowTruck
        fields = '__all__'
