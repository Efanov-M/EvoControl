from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from drivers.models import Drivers

from .forms import TowTruckAssignmentForm, TowTruckForm
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

    drivers = tow_truck.assigned_drivers.all()

    work_orders = tow_truck.work_orders.all().order_by("-created_at")

    return render(
        request,
        "fleet/fleet_detail.html",
        {
            "fleet": tow_truck,
            "drivers": drivers,
            "work_orders": work_orders,
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
        form = TowTruckAssignmentForm(
            request.POST,
            instance=tow_truck,
        )

        if form.is_valid():
            selected_drivers = form.cleaned_data["assigned_drivers"]

            selected_ids = list(selected_drivers.values_list("pk", flat=True))

            with transaction.atomic():
                form.save()

                Drivers.objects.filter(tow_truck=tow_truck).exclude(
                    pk__in=selected_ids
                ).update(tow_truck=None)

                Drivers.objects.filter(pk__in=selected_ids).update(tow_truck=tow_truck)

            return redirect(
                "fleet_detail",
                pk=tow_truck.pk,
            )

    else:
        form = TowTruckAssignmentForm(instance=tow_truck)

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
