"""
Provider serializer class definitions
"""
from rest_framework import serializers

from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    """
    Serializer for service provider model
    """
    class Meta:
        model = Provider
        fields = '__all__'
