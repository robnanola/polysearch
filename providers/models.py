"""
Provider model definitions
"""
from django.db import models
from django.core.validators import RegexValidator


class Provider(models.Model):
    """
    Service provider model definition
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message="Invalid format. ei: +999999999")
    phone_number = models.CharField(validators=[phone_validator], max_length=17, blank=True)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=25)

    def __str__(self):
        return self.name
