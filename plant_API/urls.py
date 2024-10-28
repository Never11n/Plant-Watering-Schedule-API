from django.urls import path, include
from rest_framework.routers import DefaultRouter

from plant_API.views import PlantAPIView

router = DefaultRouter()
router.register('plants', PlantAPIView)

urlpatterns = [
    path('', include(router.urls), name='plant'),
]
