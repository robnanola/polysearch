"""
Service Provider view definitions
"""
from rest_framework import viewsets

from .models import Provider
from .serializers import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    Viewset for viewing and managing providers.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
