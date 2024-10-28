from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from plant_API.serializers import PlantSerializer
from plant_API.models import Plant


class PlantAPIView(ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        plant = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(plant)
        return Response(serializer.data)

    def partial_update(self, request, pk=None, *args, **kwargs):
        plant = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(plant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PATCH'])
    def watering_plant(self, request, pk=None, *args, **kwargs):
        plant = get_object_or_404(self.queryset, pk=pk)
        if plant.is_need_be_watered:
            plant.last_watered_date = datetime.now().date()
            return Response(
                f'Plant has been watered Successfully. Next watering date: {plant.next_watering_date}',
                status=status.HTTP_200_OK
            )
        return Response(
            f'You trying to water plant to early. Next watering date: {plant.next_watering_date}',
            status=status.HTTP_400_BAD_REQUEST
        )

