from django.shortcuts import get_object_or_404, redirect, render

from operations.models import CaseStatus

from .forms import ParkingForm
from .models import ParkingLot


def parking_list(request):
    parkings = ParkingLot.objects.all()

    return render(
        request,
        "parking/parking_list.html",
        {"parking": parkings},
    )


def parking_detail(request, pk):
    parking = get_object_or_404(ParkingLot, pk=pk)

    active_cases = (
        parking.current_cases.filter(status=CaseStatus.ACTIVE)
        .select_related("vehicle")
        .order_by("-created_at", "-pk")
    )

    return render(
        request,
        "parking/parking_detail.html",
        {
            "parking": parking,
            "active_cases": active_cases,
        },
    )


def parking_create(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("parking_list")

    else:
        form = ParkingForm()

    return render(
        request,
        "parking/parking_create.html",
        {"form": form},
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
        "parking/parking_update.html",
        {"form": form},
    )


def parking_delete(request, pk):
    parking = get_object_or_404(ParkingLot, pk=pk)

    if request.method == "POST":
        parking.delete()
        return redirect("parking_list")

    return render(
        request,
        "parking/parking_delete.html",
        {"parking": parking},
    )
