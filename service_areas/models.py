"""
Service area model definitions
"""
from django.contrib.gis.db import models

from providers.models import Provider


class ServiceArea(models.Model):
    """
    Providers service area model.
    """
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    zone = models.PolygonField()

    def __str__(self):
        return "{0}: {1}".format(self.provider, self.name)
