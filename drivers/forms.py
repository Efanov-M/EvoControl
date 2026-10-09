from drivers.models import Drivers
from django.forms import ModelForm



class DriversForm(ModelForm):
    class Meta:
        model = Drivers
        fields = '__all__'
