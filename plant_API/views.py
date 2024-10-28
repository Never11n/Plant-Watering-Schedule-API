from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from plant_API.models import Plant
from plant_API.serializers import PlantSerializer


class PlantAPIView(ViewSet):
    queryset = Plant.objects.all()

    def list(self, *args, **kwargs):
        serializer = PlantSerializer(self.queryset, many=True)
        return Response(serializer.data)
