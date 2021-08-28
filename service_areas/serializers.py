"""
Service area serializer class definitions
"""
import json
from django.contrib.gis.geos import GEOSGeometry

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import ServiceArea


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """
    Serializer for ServiceArea model
    """
    zone = serializers.CharField(help_text="")

    def validate_zone(self, value):
        """
        Handles invalid value supplied.

         {"type":"Polygon","coordinates":[[
            [8.652621958553786,56.10472310840907],
            [9.234897349178786,55.960473412092604],
            [9.119540903866286,55.82185634234572],
            [8.795444224178786,55.966622682175505],
            [8.652621958553786,56.10472310840907]
            ]]}
        """
        try:
            value = json.dumps({
                "type": "Polygon",
                "coordinates": json.loads(value)
            })

            GEOSGeometry(value)
        except ValueError as validation_error:
            raise serializers.ValidationError("Invalid zone value.") from validation_error

        return value

    class Meta:
        model = ServiceArea
        geo_field = 'zone'
        fields = '__all__'

class ServiceAreaListSerializer(ServiceAreaSerializer):
    """
    Read/List serializer for service area

    We just need the return the provider's name rather than just an id
    """
    provider = serializers.StringRelatedField()
