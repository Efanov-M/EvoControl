from django.db import models
from common.validators.drivers import validate_person_name,validate_russia,validate_kazakhstan,validate_uzbekistan,validate_tajikistan,validate_armenia




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
    validators=[validate_person_name]
    )

    last_name = models.CharField("Фамилия", max_length=50, validators=[validate_person_name])

    license_driver = models.CharField("Водительское удостоверение", max_length=20, unique=True,
                                      )

    country = models.CharField('Страна выдачи водительского удостоверения',
                               max_length=20,
                                choices=DriverLicenseCountry.choices,
                                default=DriverLicenseCountry.RUSSIA
                               )

   
    def clean(self):
        validators = {
        DriverLicenseCountry.RUSSIA: validate_russia,
        DriverLicenseCountry.KAZAKHSTAN: validate_kazakhstan,
        DriverLicenseCountry.UZBEKISTAN: validate_uzbekistan,
        DriverLicenseCountry.TAJIKISTAN: validate_tajikistan,
        DriverLicenseCountry.ARMENIA: validate_armenia,
        }

        validator = validators.get(self.country)

        if validator:
            validator(self.license_driver)



   



    def __str__(self):
        return f"{self.first_name} {self.last_name} ВО :({self.license_driver}) "