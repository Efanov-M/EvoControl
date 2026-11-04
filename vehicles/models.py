from django.db import models


class Vehicle(models.Model):
    license_plate = models.CharField(
        "Госномер",
        max_length=20,
        unique=True,
    )

    brand = models.CharField(
        "Марка",
        max_length=50,
    )

    model = models.CharField(
        "Модель",
        max_length=20,
    )

    color = models.CharField(
        "Цвет",
        max_length=20,
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate}) — {self.color}"
