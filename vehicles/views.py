from django.shortcuts import render, get_object_or_404, redirect

from .models import Vehicle
from .forms import VehicleForm


def vehicle_list(request):
    vehicles = Vehicle.objects.all()

    return render(
        request,
        "vehicles/vehicle_list.html",
        {"vehicles": vehicles},
    )
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    operations = vehicle.operations.all()
    return render(
        request,
        "vehicles/vehicles_detail.html",
        {
        "vehicle": vehicle,
            "operations": operations,
        },
    )

def vehicle_create(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("vehicle_list")

    else:
        form = VehicleForm()

    return render(
        request,
        "vehicles/vehicle_create.html",
        {
            "form": form,
        },
    )


def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)

        if form.is_valid():
            form.save()
            return redirect("vehicles_detail", pk=vehicle.pk)

    else:

        form = VehicleForm(instance=vehicle)

    return render(
        request,
        "vehicles/vehicle_update.html",
        {
            "form": form,
        },
    )

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        vehicle.delete()
        return redirect("vehicle_list")


    return render(
        request,
        "vehicles/vehicle_delete.html",
        {
            "vehicle": vehicle,
        },
    )
