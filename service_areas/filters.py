"""
Service area custom serilizer filter class definitions
"""
from django_filters import rest_framework as filters
from django.contrib.gis.geos import Point

from .models import ServiceArea

class ServiceAreaFilter(filters.FilterSet):
    """
    Filter for searching coordinates/positions include the service areas defined
    """
    coords = filters.CharFilter(field_name='coords', method='filter_coordinates',
        help_text="Search service area by coordinates. Format: lat/lng (55.09/9.12)")

    @staticmethod
    def _parse_coordinates(value):
        """
        Check value if it is valid, else just return 0,0 coordinates
        """
        try:
            lat, lng = value.split('/')
            zone = Point(float(lng), float(lat))
        except (ValueError, TypeError):
            zone = Point(0,0)
        return zone

    def filter_coordinates(self, queryset, name, value):
        """
        Filter service area that contains the given coordinates
        """
        value = self._parse_coordinates(value)
        lookup = '__'.join(['zone', 'contains'])
        return queryset.filter(**{lookup: value})

    class Meta:
        model = ServiceArea
        fields = ['coords']
