from django.forms import ModelForm

from parking.models import ParkingLot


class ParkingForm(ModelForm):
    class Meta:
        model = ParkingLot
        fields = "__all__"
