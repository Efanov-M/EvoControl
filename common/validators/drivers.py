import re

from django.core.exceptions import ValidationError


def validate_person_name(value):
    for char in value:
        if not char.isalpha() and char not in " -":
            raise ValidationError(
                "Неверный формат значения: %(value)s",
                code="invalid",
                params={"value": value},
            )


def validate_license_format(value, pattern, country):
    if not re.fullmatch(pattern, value):
        raise ValidationError(
            "Неверный формат водительского удостоверения (%(country)s): %(value)s",
            code="invalid_license",
            params={"country": country, "value": value},
        )


def validate_russia(value):
    # 10 цифр
    validate_license_format(value, r"[0-9]{10}", "Россия")


def validate_kazakhstan(value):
    # Временная упрощённая проверка:
    # от 1 до 20 латинских букв или цифр
    validate_license_format(value, r"[A-Z0-9]{1,20}", "Казахстан")


def validate_uzbekistan(value):
    # 2 латинские буквы + 6 цифр
    validate_license_format(value, r"[A-Z]{2}[0-9]{6}", "Узбекистан")


def validate_tajikistan(value):
    # 2 латинские буквы + 7 цифр
    validate_license_format(value, r"[A-Z]{2}[0-9]{7}", "Таджикистан")


def validate_armenia(value):
    # Предварительное учебное правило:
    # 2 латинские буквы + 6 цифр
    validate_license_format(value, r"[A-Z]{2}[0-9]{6}", "Армения")
