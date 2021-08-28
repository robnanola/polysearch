"""
Service area view definitions
"""
from rest_framework import viewsets

from .models import ServiceArea
from .serializers import ServiceAreaSerializer, ServiceAreaListSerializer
from .filters import ServiceAreaFilter

class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    Viewset for viewing and managing service areas.
    """
    queryset = ServiceArea.objects.prefetch_related('provider')
    default_serializer_class = ServiceAreaSerializer
    serializer_classes = {
        'list': ServiceAreaListSerializer
    }
    filterset_class = ServiceAreaFilter

    def get_serializer_class(self):
        """
        Returns the serializer class depending on view action
        """
        return self.serializer_classes.get(self.action, self.default_serializer_class)
