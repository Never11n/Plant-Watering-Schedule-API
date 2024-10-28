from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from plant_API.models import Plant
from plant_API.serializers import PlantSerializer


class PlantAPIView(ViewSet):
    queryset = Plant.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = PlantSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        plant = get_object_or_404(self.queryset, pk=pk)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
