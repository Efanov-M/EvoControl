from django.shortcuts import render, get_object_or_404, redirect

from .models import TowTruck
from .forms import TowTruckForm


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

def fleet_create(request):
    if request.method == "POST":
        form = TowTruckForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("fleet_list")

    else:
        form = TowTruckForm()

    return render(
        request,
        "fleet/fleet_create.html",
        {
            "form": form,
        },
    )


def fleet_update(request, pk):
    tow_truck = get_object_or_404(TowTruck, pk=pk)
    if request.method == "POST":
        form = TowTruckForm(request.POST, instance=tow_truck)

        if form.is_valid():
            form.save()
            return redirect("fleet_detail", pk=tow_truck.pk)

    else:

        form = TowTruckForm(instance=tow_truck)

    return render(
        request,
        "fleet/fleet_update.html",
        {
            "form": form,
        },
    )

def fleet_delete(request, pk):
    tow_truck = get_object_or_404(TowTruck, pk=pk)
    if request.method == "POST":
        tow_truck.delete()
        return redirect("fleet_list")


    return render(
        request,
        "fleet/fleet_delete.html",
        {
            "fleet": tow_truck,
        },
    )
