from django.db import models

from common.validators.drivers import (
    validate_person_name,
)
from config import settings
from parking.models import ParkingLot


# Create your models here.
class Dispatchers(models.Model):
    first_name = models.CharField(
        "Имя", max_length=50, validators=[validate_person_name]
    )

    last_name = models.CharField(
        "Фамилия", max_length=50, validators=[validate_person_name]
    )

    place_work = models.ForeignKey(
        ParkingLot, on_delete=models.PROTECT, verbose_name="Место работы"
    )

    employee_number = models.CharField("Табельный номер", max_length=10, unique=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dispatcher_profile",
        verbose_name="Учётная запись",
    )
