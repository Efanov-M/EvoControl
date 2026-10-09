from django.db import models





class Drivers(models.Model):

    first_name = models.CharField(
    "Имя",
    max_length=50,
    )

    last_name = models.CharField("Фамилия", max_length=50)

    license_driver = models.CharField("Водительское удостоверение", max_length=20, unique=True)

   



    def __str__(self):
        return f"{self.first_name} {self.last_name} ВО :({self.license_driver}) "