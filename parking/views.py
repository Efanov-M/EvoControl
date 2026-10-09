from django.shortcuts import render, get_object_or_404, redirect

from .models import ParkingLot
from .forms import ParkingForm



def parking_list(request):
    parkings = ParkingLot.objects.all()

    return render(
        request,
        "parking/parking_list.html",
        {"parking": parkings},
    )

def parking_detail(request, pk):
    parking = get_object_or_404(ParkingLot, pk=pk)
    operations = parking.operations.all()
    return render(
        request,
        "parking/parking_detail.html",
        {
        "parking": parking,
            "operations": operations,
        },
    )


def parking_create(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("drivers_list")

    else:
        form = ParkingForm()

    return render(
        request,
        "parking/parking_create.html",
        {
            "form": form,
        },
    )


def parking_update(request, pk):
    parking = get_object_or_404(ParkingLot, pk=pk)
    if request.method == "POST":
        form = ParkingForm(request.POST, instance=parking)

        if form.is_valid():
            form.save()
            return redirect("parking_detail", pk=parking.pk)

    else:

        form = ParkingForm(instance=parking)

    return render(
        request,
        "vehicles/vehicle_update.html",
        {
            "form": form,
        },
    )

def parking_delete(request, pk):
    parking = get_object_or_404(ParkingLot, pk=pk)
    if request.method == "POST":
        parking.delete()
        return redirect("parkinglist")


    return render(
        request,
        "parking/parking_delete.html",
        {
            "parking": parking,
        },
    )
