from django.forms import ModelForm

from dispatchers.models import Dispatchers


class DispatcherForm(ModelForm):
    class Meta:
        model = Dispatchers
        fields = ["first_name", "last_name", "place_work", "employee_number"]
