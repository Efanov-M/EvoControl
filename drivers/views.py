from django.shortcuts import render, get_object_or_404, redirect

from .models import Drivers
from .forms import DriversForm


def drivers_list(request):
    drivers = Drivers.objects.all()

    return render(
        request,
        "drivers/drivers_list.html",
        {"drivers": drivers},
    )


def driver_detail(request, pk):
    driver = get_object_or_404(Drivers, pk=pk)
    operations = driver.operations.all()
    return render(
        request,
        "drivers/driver_detail.html",
        {
        "driver": driver,
        "operations": operations,
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
        {
            "form": form,
        },
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
        {
            "form": form,
        },
    )

def driver_delete(request, pk):
    driver = get_object_or_404(Drivers, pk=pk)
    if request.method == "POST":
        driver.delete()
        return redirect("drivers_list")


    return render(
        request,
        "drivers/driver_delete.html",
        {
            "driver": driver,
        },
    )
