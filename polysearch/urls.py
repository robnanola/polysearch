"""polysearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from providers.views import ProviderViewSet
from rest_framework.routers import DefaultRouter
from service_areas.views import ServiceAreaViewSet



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'service-area', ServiceAreaViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
