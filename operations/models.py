from django.conf import settings
from django.db import models

from drivers.models import Drivers
from fleet.models import TowTruck
from parking.models import ParkingLot
from vehicles.models import Vehicle


class OperationType(models.TextChoices):
    EVACUATION = "evacuation", "Эвакуация"
    ARRIVAL = "arrival", "Приём"
    TRANSFER = "transfer", "Перемещение"
    RELEASE = "release", "Выдача"


class CaseStatus(models.TextChoices):
    ACTIVE = "active", "Активен"
    CLOSED = "closed", "Закрыт"


class EvacuationCase(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name="evacuation_cases",
        verbose_name="Автомобиль",
    )
    status = models.CharField(
        "Статус", max_length=20, choices=CaseStatus.choices, default=CaseStatus.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)


class VehicleOperation(models.Model):
    tow_truck = models.ForeignKey(
        TowTruck,
        on_delete=models.PROTECT,
        related_name="operations",
        verbose_name="Эвакуатор",
        null=True,
        blank=True,
    )
    evacuation_case = models.ForeignKey(
        EvacuationCase,
        on_delete=models.PROTECT,
        related_name="operations",
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
        related_name="operations",
        verbose_name="Водители",
    )

    def __str__(self):
        return (
            f"{self.evacuation_case} — "
            f"{self.get_operation_type_display()} — "
            f"{self.created_at:%d.%m.%Y %H:%M}"
        )
