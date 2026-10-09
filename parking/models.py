from django.db import models

class ParkingLot(models.Model):
    name = models.CharField("Наименование стоянки", max_length=50)
    address = models.TextField("Адрес стоянки")
    is_active = models.BooleanField(
    "Активна",
    default=True
    )

    def __str__(self):
        return self.name




