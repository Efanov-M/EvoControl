from django.db import models

from dispatchers.models import Dispatchers
from drivers.models import Drivers
from fleet.models import TowTruck


class StatusOrder(models.TextChoices):
    CREATED = "created", "Создан"
    ASSIGNED = "assigned", "Назначен"
    IN_PROGRESS = "in_progress", "Выполняется"
    COMPLETED = "completed", "Выполнен"
    CANCELED = "cancelled", "Отменён"


class WorkOrder(models.Model):
    address = models.CharField(
        "Адрес эвакуации",
        max_length=255,
    )

    driver = models.ForeignKey(
        Drivers,
        on_delete=models.PROTECT,
        related_name="work_orders",
        verbose_name="Водитель",
    )

    tow_truck = models.ForeignKey(
        TowTruck,
        on_delete=models.PROTECT,
        related_name="work_orders",
        verbose_name="Эвакуатор",
    )

    dispatcher = models.ForeignKey(
        Dispatchers,
        on_delete=models.PROTECT,
        related_name="work_orders",
        verbose_name="Ответственный диспетчер",
    )

    status = models.CharField(
        "Статус наряда",
        max_length=20,
        choices=StatusOrder.choices,
        default=StatusOrder.CREATED,
    )

    created_at = models.DateTimeField(
        "Дата и время создания наряда",
        auto_now_add=True,
    )

    comment = models.TextField(
        "Комментарий",
        blank=True,
    )

    def __str__(self):
        return f"Наряд №{self.pk} — {self.address} — {self.get_status_display()}"
