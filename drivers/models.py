from django.core.exceptions import ValidationError
from django.db import models

from common.validators.drivers import (
    validate_armenia,
    validate_kazakhstan,
    validate_person_name,
    validate_russia,
    validate_tajikistan,
    validate_uzbekistan,
)
from fleet.models import TowTruck


class DriverLicenseCountry(models.TextChoices):
    RUSSIA = "Russia", "Россия"
    KAZAKHSTAN = "Kazakhstan", "Казахстан"
    UZBEKISTAN = "Uzbekistan", "Узбекистан"
    TAJIKISTAN = "Tajikistan", "Таджикистан"
    ARMENIA = "Armenia", "Армения"


class Drivers(models.Model):
    first_name = models.CharField(
        "Имя",
        max_length=50,
        validators=[validate_person_name],
    )

    last_name = models.CharField(
        "Фамилия",
        max_length=50,
        validators=[validate_person_name],
    )

    license_driver = models.CharField(
        "Водительское удостоверение",
        max_length=20,
        unique=True,
    )

    country = models.CharField(
        "Страна выдачи водительского удостоверения",
        max_length=20,
        choices=DriverLicenseCountry.choices,
        default=DriverLicenseCountry.RUSSIA,
    )

    tow_truck = models.ForeignKey(
        TowTruck,
        on_delete=models.PROTECT,
        related_name="assigned_drivers",
        verbose_name="Закреплённый эвакуатор",
        null=True,
        blank=True,
    )

    def clean(self):
        validators = {
            DriverLicenseCountry.RUSSIA: validate_russia,
            DriverLicenseCountry.KAZAKHSTAN: validate_kazakhstan,
        }

        validator = validators.get(self.country)

        if validator:
            try:
                validator(self.license_driver)
            except ValidationError as error:
                raise ValidationError({"license_driver": error}) from error

    def __str__(self):
        return f"{self.first_name} {self.last_name} ВО: ({self.license_driver})"
