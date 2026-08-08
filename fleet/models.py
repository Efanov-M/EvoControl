from django.db import models

# Create your models here.
class TruckType(models.TextChoices):
    PLATFORM = "platform", "Платформа"
    MANIPULATOR = "manipulator", "Манипулятор"


class TowTruck(models.Model):
    license_plate = models.CharField(
    "Госномер",
    max_length=20,
    unique=True
    )

    brand = models.CharField(
    "Марка",
    max_length=50
    )

    truck_type = models.CharField(
    "Тип эвакуатора",
    max_length=20,
    choices=TruckType.choices,
    default=TruckType.PLATFORM
)
    model = models.CharField("Модель", max_length=20,blank=True)

    vin = models.CharField(max_length=17,blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.model:
            return f"{self.brand} {self.model} ({self.license_plate})"

        return f"{self.brand} ({self.license_plate})"



