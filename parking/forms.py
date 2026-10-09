from parking.models import ParkingLot
from django.forms import ModelForm



class ParkingForm(ModelForm):
    class Meta:
        model = ParkingLot
        fields = '__all__'
