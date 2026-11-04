from django.forms import ModelForm

from drivers.models import Drivers


class DriversForm(ModelForm):
    class Meta:
        model = Drivers
        fields = "__all__"
