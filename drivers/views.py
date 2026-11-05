from django.shortcuts import get_object_or_404, redirect, render

from .forms import DriversForm
from .models import Drivers


def drivers_list(request):
    drivers = Drivers.objects.all()

    return render(
        request,
        "drivers/drivers_list.html",
        {"drivers": drivers},
    )


def driver_detail(request, pk):
    driver = get_object_or_404(
        Drivers.objects.select_related("tow_truck"),
        pk=pk,
    )

    work_orders = driver.work_orders.select_related("tow_truck").order_by(
        "-created_at", "-pk"
    )

    return render(
        request,
        "drivers/driver_detail.html",
        {
            "driver": driver,
            "work_orders": work_orders,
        },
    )


def driver_create(request):
    if request.method == "POST":
        form = DriversForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("drivers_list")

    else:
        form = DriversForm()

    return render(
        request,
        "drivers/driver_create.html",
        {"form": form},
    )


def driver_update(request, pk):
    driver = get_object_or_404(Drivers, pk=pk)

    if request.method == "POST":
        form = DriversForm(request.POST, instance=driver)

        if form.is_valid():
            form.save()
            return redirect("driver_detail", pk=driver.pk)

    else:
        form = DriversForm(instance=driver)

    return render(
        request,
        "drivers/driver_update.html",
        {"form": form},
    )


def driver_delete(request, pk):
    driver = get_object_or_404(Drivers, pk=pk)

    if request.method == "POST":
        driver.delete()
        return redirect("drivers_list")

    return render(
        request,
        "drivers/driver_delete.html",
        {"driver": driver},
    )
