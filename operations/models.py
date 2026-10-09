from django.conf import settings
from django.db import models

from fleet.models import TowTruck
from vehicles.models import Vehicle
from drivers.models import Drivers


class OperationType(models.TextChoices):
    ARRIVAL = "arrival", "Приём"
    TRANSFER = "transfer", "Перемещение"
    RELEASE = "release", "Выдача"

class VehicleOperation(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name="operations",
        verbose_name="Автомобиль",
    )

    tow_truck = models.ForeignKey(
        TowTruck,
        on_delete=models.PROTECT,
        related_name="operations",
        verbose_name="Эвакуатор",
        blank=True,
        null=True,
    )

    dispatcher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="handled_operations",
        verbose_name="Диспетчер",
    )

    operation_type = models.CharField(
        "Тип операции",
        max_length=20,
        choices=OperationType.choices,
    )

    created_at = models.DateTimeField(
        "Дата и время операции",
        auto_now_add=True,
    )

    comment = models.TextField(
        "Комментарий",
        blank=True,
    )
    parking_lot = models.ForeignKey(
        ParkingLot,
        on_delete=models.PROTECT,
        related_name="operations",
        verbose_name="Стоянка",
        null=True,
        blank=True,
    )
    driver = models.ForeignKey(
            Drivers,
            on_delete=models.PROTECT,
            related_name= "operations",
            verbose_name= "Водители"
        )
    

    def __str__(self):
        return (
            f"{self.vehicle} — "
            f"{self.get_operation_type_display()} — "
            f"{self.created_at:%d.%m.%Y %H:%M}"
        )
