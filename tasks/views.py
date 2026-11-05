from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from tasks.forms import WorkOrder, WorkOrderForm

# Create your views here.


def work_order_list(request):
    work_orders = WorkOrder.objects.all()
    search = request.GET.get("search", "").strip()
    if search:
        search_filter = Q(address__icontains=search)

        if search.isdigit():
            search_filter |= Q(pk=int(search))

        work_orders = work_orders.filter(search_filter)
    allowed_sorts = ("status", "-status", "driver")
    sort = request.GET.get("sort")
    if sort not in allowed_sorts:
        sort = "status"
    work_orders = work_orders.order_by(sort)
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
        },
    )


def work_order_create(request):
    if request.method == "POST":
        form = WorkOrderForm(request.POST)

        if form.is_valid():
            form.save()
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
        "task/work_order_detail.html",
        {
            "task": task,
        },
    )


def work_order_updated(request, pk):
    task = get_object_or_404(WorkOrder, pk=pk)
    if request.method == "POST":
        form = WorkOrderForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("work_order_detail", pk=task.pk)

    else:
        form = WorkOrderForm(instance=task)

    return render(
        request,
        "task/work_order_updated.html",
        {
            "task": task,
        },
    )


def work_order_cancel(): ...
def work_order_start(): ...
def work_order_complete(): ...
