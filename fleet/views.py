from django.shortcuts import render, get_object_or_404

from .models import TowTruck


def fleet_list(request):
    tow_trucks = TowTruck.objects.all()

    return render(
        request,
        "fleet/fleet_list.html",
        {"fleet": tow_trucks},
    )
def fleet_detail(request, pk):
    tow_truck = get_object_or_404(TowTruck, pk=pk)
    operations = tow_truck.operations.all()
    return render(
        request,
        "fleet/fleet_detail.html",
        {
        "fleet": tow_truck,
        "operations": operations,
        },
    )
