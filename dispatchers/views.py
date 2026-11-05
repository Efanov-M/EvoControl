from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DispatcherForm
from .models import Dispatchers


def dispatchers_list(request):
    dispatchers = Dispatchers.objects.all()

    search = request.GET.get("search", "").strip()

    if search:
        dispatchers = dispatchers.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(employee_number__icontains=search)
        )

    allowed_sorts = ("last_name", "-last_name", "employee_number")
    sort = request.GET.get("sort")

    if sort not in allowed_sorts:
        sort = "last_name"

    dispatchers = dispatchers.order_by(sort, "pk")

    paginator = Paginator(dispatchers, 15)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(
        request,
        "dispatchers/dispatchers_list.html",
        {
            "dispatchers": page,
            "sort": sort,
            "search": search,
        },
    )


def dispatcher_detail(request, pk):
    dispatcher = get_object_or_404(
        Dispatchers.objects.select_related("place_work"),
        pk=pk,
    )

    work_orders = dispatcher.work_orders.select_related("driver", "tow_truck").order_by(
        "-created_at", "-pk"
    )

    return render(
        request,
        "dispatchers/dispatcher_detail.html",
        {
            "dispatcher": dispatcher,
            "work_orders": work_orders,
        },
    )


def dispatcher_create(request):
    if request.method == "POST":
        form = DispatcherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dispatchers_list")

    else:
        form = DispatcherForm()

    return render(
        request,
        "dispatchers/dispatcher_create.html",
        {"form": form},
    )


def dispatcher_update(request, pk):
    dispatcher = get_object_or_404(Dispatchers, pk=pk)

    if request.method == "POST":
        form = DispatcherForm(request.POST, instance=dispatcher)

        if form.is_valid():
            form.save()
            return redirect("dispatcher_detail", pk=dispatcher.pk)

    else:
        form = DispatcherForm(instance=dispatcher)

    return render(
        request,
        "dispatchers/dispatcher_update.html",
        {"form": form},
    )


def dispatcher_delete(request, pk):
    dispatcher = get_object_or_404(Dispatchers, pk=pk)

    if request.method == "POST":
        dispatcher.delete()
        return redirect("dispatchers_list")

    return render(
        request,
        "dispatchers/dispatcher_delete.html",
        {"dispatcher": dispatcher},
    )
