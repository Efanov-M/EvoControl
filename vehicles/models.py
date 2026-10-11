from django.db import models
from vehicles.validators import validate_license_plate

# Create your models here.




class Vehicle(models.Model):
    license_plate = models.CharField(
    "Госномер",
    max_length=20,
    unique=True,
    validators=[validate_license_plate]
    )

    brand = models.CharField("Марка", max_length=50)

    model = models.CharField("Модель", max_length=20)

    color = models.CharField("Цвет", max_length=20)

    legal_basis = models.CharField("Статья изъятия", max_length=20)

    was_in_accident = models.BooleanField("Была ли в ДТП", default=False)



    def __str__(self):
        if self.was_in_accident:
            return f"{self.brand} {self.model} ({self.license_plate}) {self.color} {self.legal_basis}ДТП"

        return f"{self.brand} {self.model} ({self.license_plate}) {self.color} {self.legal_basis}"
