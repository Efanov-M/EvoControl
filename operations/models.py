from django.db import models

from dispatchers.models import Dispatchers
from drivers.models import Drivers
from fleet.models import TowTruck
from parking.models import ParkingLot
from tasks.models import WorkOrder
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

    work_order = models.OneToOneField(
        WorkOrder,
        on_delete=models.PROTECT,
        related_name="evacuation_case",
        verbose_name="Наряд-задание",
        null=True,
        blank=True,
    )

    status = models.CharField(
        "Статус дела",
        max_length=20,
        choices=CaseStatus.choices,
        default=CaseStatus.ACTIVE,
    )

    current_parking = models.ForeignKey(
        ParkingLot,
        on_delete=models.PROTECT,
        related_name="current_cases",
        verbose_name="Текущая стоянка",
        null=True,
        blank=True,
    )

    legal_basis = models.CharField(
        "Статья изъятия",
        max_length=20,
    )

    was_in_accident = models.BooleanField(
        "Была ли в ДТП",
        default=False,
    )

    created_at = models.DateTimeField(
        "Дата и время открытия дела",
        auto_now_add=True,
    )

    def __str__(self):
        return f"Дело №{self.pk} — {self.vehicle} — {self.get_status_display()}"


class VehiclePhoto(models.Model):
    evacuation_case = models.ForeignKey(
        EvacuationCase,
        on_delete=models.PROTECT,
        related_name="photos",
        verbose_name="Дело эвакуации",
    )

    image = models.ImageField(
        "Фотография",
        upload_to="evacuations/photos/%Y/%m/%d/",
    )

    created_at = models.DateTimeField(
        "Дата и время добавления",
        auto_now_add=True,
    )

    def __str__(self):
        return f"Фотография №{self.pk} — дело №{self.evacuation_case_id}"


class VehicleOperation(models.Model):
    evacuation_case = models.ForeignKey(
        EvacuationCase,
        on_delete=models.PROTECT,
        related_name="operations",
        verbose_name="Дело эвакуации",
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

    def __str__(self):
        return f"Операция №{self.pk} — {self.get_operation_type_display()}"


class EvacuationOperation(models.Model):
    operation = models.OneToOneField(
        VehicleOperation,
        on_delete=models.PROTECT,
        related_name="evacuation_detail",
        verbose_name="Операция",
    )

    driver = models.ForeignKey(
        Drivers,
        on_delete=models.PROTECT,
        related_name="evacuations",
        verbose_name="Водитель",
    )

    tow_truck = models.ForeignKey(
        TowTruck,
        on_delete=models.PROTECT,
        related_name="evacuations",
        verbose_name="Эвакуатор",
    )

    dispatcher = models.ForeignKey(
        Dispatchers,
        on_delete=models.PROTECT,
        related_name="evacuations",
        verbose_name="Ответственный диспетчер",
    )

    def __str__(self):
        return f"Эвакуация — операция №{self.operation_id}"


class ArrivalOperation(models.Model):
    operation = models.OneToOneField(
        VehicleOperation,
        on_delete=models.PROTECT,
        related_name="arrival_detail",
        verbose_name="Операция",
    )

    driver = models.ForeignKey(
        Drivers,
        on_delete=models.PROTECT,
        related_name="arrivals",
        verbose_name="Водитель",
    )

    tow_truck = models.ForeignKey(
        TowTruck,
        on_delete=models.PROTECT,
        related_name="arrivals",
        verbose_name="Эвакуатор",
        null=True,
        blank=True,
    )

    dispatcher = models.ForeignKey(
        Dispatchers,
        on_delete=models.PROTECT,
        related_name="arrivals",
        verbose_name="Принимающий диспетчер",
    )

    parking_lot = models.ForeignKey(
        ParkingLot,
        on_delete=models.PROTECT,
        related_name="arrivals",
        verbose_name="Стоянка приёма",
    )

    def __str__(self):
        return f"Приём — операция №{self.operation_id} — {self.parking_lot}"


class TransferOperation(models.Model):
    operation = models.OneToOneField(
        VehicleOperation,
        on_delete=models.PROTECT,
        related_name="transfer_detail",
        verbose_name="Операция",
    )

    driver = models.ForeignKey(
        Drivers,
        on_delete=models.PROTECT,
        related_name="transfers",
        verbose_name="Водитель",
    )

    tow_truck = models.ForeignKey(
        TowTruck,
        on_delete=models.PROTECT,
        related_name="transfers",
        verbose_name="Эвакуатор",
    )

    dispatcher = models.ForeignKey(
        Dispatchers,
        on_delete=models.PROTECT,
        related_name="transfers",
        verbose_name="Ответственный диспетчер",
    )

    from_parking = models.ForeignKey(
        ParkingLot,
        on_delete=models.PROTECT,
        related_name="outgoing_transfers",
        verbose_name="Стоянка отправления",
    )

    to_parking = models.ForeignKey(
        ParkingLot,
        on_delete=models.PROTECT,
        related_name="incoming_transfers",
        verbose_name="Стоянка назначения",
    )

    def __str__(self):
        return (
            f"Перемещение №{self.operation_id}: {self.from_parking} → {self.to_parking}"
        )


class ReleaseOperation(models.Model):
    operation = models.OneToOneField(
        VehicleOperation,
        on_delete=models.PROTECT,
        related_name="release_detail",
        verbose_name="Операция",
    )

    dispatcher = models.ForeignKey(
        Dispatchers,
        on_delete=models.PROTECT,
        related_name="releases",
        verbose_name="Диспетчер выдачи",
    )

    parking_lot = models.ForeignKey(
        ParkingLot,
        on_delete=models.PROTECT,
        related_name="releases",
        verbose_name="Стоянка выдачи",
    )

    def __str__(self):
        return f"Выдача — операция №{self.operation_id} — {self.parking_lot}"
