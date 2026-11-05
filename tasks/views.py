from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from tasks.forms import WorkOrderForm
from tasks.models import StatusOrder, WorkOrder


def work_order_list(request):
    tab = request.GET.get("tab", "active")

    if tab == "archive":
        work_orders = WorkOrder.objects.filter(
            status__in=[
                StatusOrder.COMPLETED,
                StatusOrder.CANCELED,
            ]
        )
    else:
        tab = "active"
        work_orders = WorkOrder.objects.filter(
            status__in=[
                StatusOrder.CREATED,
                StatusOrder.ASSIGNED,
                StatusOrder.IN_PROGRESS,
            ]
        )

    search = request.GET.get("search", "").strip()

    if search:
        search_filter = Q(address__icontains=search)

        if search.isdigit():
            search_filter |= Q(pk=int(search))

        work_orders = work_orders.filter(search_filter)

    allowed_sorts = (
        "-created_at",
        "created_at",
        "status",
        "driver",
    )

    sort = request.GET.get("sort")

    if sort not in allowed_sorts:
        sort = "-created_at"

    work_orders = work_orders.order_by(sort, "-pk")

    paginator = Paginator(work_orders, 5)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(
        request,
        "tasks/work_order_list.html",
        {
            "work_orders": page,
            "sort": sort,
            "search": search,
            "tab": tab,
        },
    )


def work_order_create(request):
    if request.method == "POST":
        form = WorkOrderForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.tow_truck = form.cleaned_data["driver"].tow_truck

            task.save()
            return redirect("work_order_list")

    else:
        form = WorkOrderForm()

    return render(
        request,
        "tasks/work_order_form.html",
        {
            "form": form,
        },
    )


def work_order_detail(request, pk):
    task = get_object_or_404(WorkOrder, pk=pk)

    return render(
        request,
        "tasks/work_order_detail.html",
        {
            "task": task,
        },
    )


def work_order_update(request, pk):
    task = get_object_or_404(WorkOrder, pk=pk)
    original_driver_id = task.driver_id

    if request.method == "POST":
        form = WorkOrderForm(request.POST, instance=task)

        if form.is_valid():
            task = form.save(commit=False)

            if task.driver_id != original_driver_id:
                task.tow_truck = task.driver.tow_truck

            task.save()

            return redirect("work_order_detail", pk=task.pk)

    else:
        form = WorkOrderForm(instance=task)

    return render(
        request,
        "tasks/work_order_updated.html",
        {
            "form": form,
            "task": task,
        },
    )


@require_POST
def work_order_assign(request, pk):
    task = get_object_or_404(WorkOrder, pk=pk)

    if task.status == StatusOrder.CREATED:
        task.status = StatusOrder.ASSIGNED
        task.save(update_fields=["status"])
        messages.success(request, "Наряд назначен к выполнению")

    else:
        messages.error(
            request,
            "Невозможно назначить наряд с текущим статусом",
        )

    return redirect("work_order_detail", pk=task.pk)


@require_POST
def work_order_start(request, pk):
    task = get_object_or_404(WorkOrder, pk=pk)

    if task.status == StatusOrder.ASSIGNED:
        task.status = StatusOrder.IN_PROGRESS
        task.save(update_fields=["status"])
        messages.success(request, "Наряд передан в работу")

    else:
        messages.error(
            request,
            "Нельзя начать выполнение наряда с текущим статусом",
        )

    return redirect("work_order_detail", pk=task.pk)


@require_POST
def work_order_complete(request, pk):
    task = get_object_or_404(WorkOrder, pk=pk)

    if task.status == StatusOrder.IN_PROGRESS:
        task.status = StatusOrder.COMPLETED
        task.save(update_fields=["status"])
        messages.success(request, "Наряд успешно завершён")

    else:
        messages.error(
            request,
            "Нельзя завершить наряд с текущим статусом",
        )

    return redirect("work_order_detail", pk=task.pk)


@require_POST
def work_order_cancel(request, pk):
    task = get_object_or_404(WorkOrder, pk=pk)

    if task.status not in (
        StatusOrder.COMPLETED,
        StatusOrder.CANCELED,
    ):
        task.status = StatusOrder.CANCELED
        task.save(update_fields=["status"])
        messages.success(request, "Наряд отменён")

    else:
        messages.error(
            request,
            "Нельзя отменить наряд с текущим статусом",
        )

    return redirect("work_order_detail", pk=task.pk)
